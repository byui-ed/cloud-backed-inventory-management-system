import time
import firebase_admin
from firebase_admin import credentials, firestore
from google.api_core.exceptions import GoogleAPIError

# Initialize Firestore SDK
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
db = firestore.client()


class InventoryService:
    def __init__(self):
        self.collection = db.collection('inventory')
        self._listener_watch = None

    def get_low_inventory_items(self):
        """Retrieves documents where quantity < reorder_threshold."""
        try:
            docs = self.collection.stream()
            low_stock = []
            
            for doc in docs:
                data = doc.to_dict()
                qty = data.get('quantity', 0)
                threshold = data.get('reorder_threshold', 0)
                
                if qty < threshold:
                    low_stock.append({**data, "sku": doc.id})
                    
            return low_stock
        except GoogleAPIError as e:
            print(f"Firestore Query Error: {e}")
            raise

    def subscribe_to_inventory_updates(self):
        """Subscribes to real-time inventory updates and logs stock changes."""
        
        def on_snapshot(col_snapshot, changes, read_time):
            for change in changes:
                doc_data = change.document.to_dict()
                sku = change.document.id

                if change.type.name == 'ADDED':
                    print(f"🔔 [NEW ITEM ADDED]: {sku} - {doc_data.get('name', 'N/A')}")
                
                elif change.type.name == 'MODIFIED':
                    qty = doc_data.get('quantity', 0)
                    threshold = doc_data.get('reorder_threshold', 0)
                    print(f"🔄 [ITEM UPDATED]: {sku} | Quantity: {qty}")
                    
                    if qty < threshold:
                        print(f"⚠️ [LOW STOCK ALERT]: {sku} ({qty} < {threshold})")

                elif change.type.name == 'REMOVED':
                    print(f"❌ [ITEM DELETED]: {sku}")

        # Attach real-time listener
        self._listener_watch = self.collection.on_snapshot(on_snapshot)
        print("Listening for real-time inventory updates...")
        return self._listener_watch

    def unsubscribe(self):
        """Detaches the active real-time listener."""
        if self._listener_watch:
            self._listener_watch.unsubscribe()
            print("Unsubscribed from real-time inventory updates.")


# --- Example Usage ---
if __name__ == "__main__":
    service = InventoryService()

    # 1. Start real-time subscription
    service.subscribe_to_inventory_updates()

    # 2. Perform low-inventory query
    low_stock = service.get_low_inventory_items()
    print("Initial Low Stock Items:", low_stock)

    # Keep script running to receive live events
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        service.unsubscribe()