# Overview

As a software engineer, this project serves to expand my hands-on experience with cloud-native data architecture and serverless database integrations. The primary goal is to build a reliable backend pipeline that interacts directly with fully managed cloud datastores, mastering asynchronous data operations, real-time synchronization, and cloud authentication patterns.

This software is a Python-based command-line interface (CLI) application that integrates with Google Cloud Firestore, a NoSQL document database. The application performs full Create, Read, Update, and Delete (CRUD) operations on cloud-hosted document collections. Users can interact with the system via a terminal menu to create new entity records, query existing collections, update specific document fields using batch operations, and delete entries safely.

The purpose of writing this software is to gain practical proficiency in integrating Python backends with cloud NoSQL databases, understanding document-oriented schema design, and handling distributed database operations securely using service account credentials.


[Software Demo Video](https://youtu.be/CC2Dcvz6gfM)

# Cloud Database

This application utilizes Google Cloud Firestore in Native mode. Firestore is a scalable, serverless NoSQL document database designed for high availability, automatic scaling, and real-time synchronization across client applications.

The database follows a document-collection structure:

Collections: Top-level containers (e.g., projects or users) that store individual records.

Documents: JSON-like records stored inside collections. Each document contains key-value pairs representing entity attributes (such as title as a String, status as a String, tags as an Array, and last_updated as a Timestamp).

Sub-collections: Hierarchical structures nested within individual documents to model one-to-many relationships without flattening data schemas.

# Development Environment

The development environment was configured locally using Visual Studio Code and Python's virtual environment tool (venv) to isolate dependencies.

Language: Python 3

Tools & Utilities: Git/GitHub for version control, Google Cloud Console for service account IAM configuration and database monitoring, and Google Cloud SDK (gcloud CLI).

Libraries & Packages:

google-cloud-firestore: The official Python SDK for executing database operations and listeners against Firestore.

google-auth: Handles authentication via GCP service account JSON key pairs.

python-dotenv: Manages environment variables and keeps sensitive cloud credentials out of source control.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Web Site Name](https://www.google.com/search?q=https://cloud.google.com/python/docs/reference/firestore/latest)
- [Web Site Name](https://firebase.google.com/docs/firestore)
-  [Web Site Name](https://www.google.com/search?q=https://google-auth.readthedocs.io/en/latest/)

# Future Work

Implement real-time document listeners (on_snapshot) to enable live push notifications when cloud data updates.

Add robust input validation and schema enforcement using pydantic prior to database writes.

Build a web-based dashboard using Express.js or Streamlit to visualize the Firestore collections in a browser interface.
