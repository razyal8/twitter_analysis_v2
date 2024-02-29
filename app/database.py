import logging

from pymongo import MongoClient

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

def check_mongodb_health(client):
    try:
        # Use the 'admin' database to check MongoDB health
        admin_db = client.admin
        admin_db.command("ping")  # Ping MongoDB to check connection
        logging.info("MongoDB connection is healthy")
        return True
    except Exception as e:
        logging.error(f"Error checking MongoDB health: {str(e)}")
        return False

def perform_mongodb_operations():
    # MongoDB connection URI
    MONGO_URI = "mongodb://mongodb:27017/"  # Assuming MongoDB service is named 'mongodb'
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)

    try:

        if not check_mongodb_health(client):
            return "MongoDB connection is not healthy"
        
        logging.info("connected to db")
       # Accessing the database
        db = client["test-tweets"]  # Use the correct database name

        # Accessing the collection
        collection = db["tweets"]  # Use the correct collection name

        logging.info("start insert")
        # Inserting a document
        post = {"author": "razy", "text": "Hello, MongoDB!"}
        collection.insert_one(post)
        logging.info("Inserted a document")

        # Querying documents
        cursor = collection.find({})
        for document in cursor:
            logging.info(f"Queried document: {document}")

        # Updating a document
        collection.update_one({"author": "razy"}, {"$set": {"text": "Hello, Updated MongoDB!"}})
        logging.info("Updated a document")

        # Querying documents after update
        results = []
        cursor = collection.find({})
        for document in cursor:
            logging.info(f"Queried document after update: {document}")
            results.append(document)

        return results

    except Exception as e:
        logging.error(f"Error performing MongoDB operations: {str(e)}")
        return f"Error performing MongoDB operations: {str(e)}"
    
    finally:
        # Closing connection
        client.close()
