from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri='mongodb://mongodb:27017/', db_name='Tweets_Dataset'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        query = {"id": document["id"]}
        update = {"$setOnInsert": document}
        result = collection.update_one(query, update, upsert=True)
        return result.upserted_id is not None

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def find_many(self, collection_name, query):
        collection = self.db[collection_name]
        return list(collection.find(query))

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        result = collection.update_one(query, {'$set': update})
        return result.modified_count

    def update_many(self, collection_name, query, update):
        collection = self.db[collection_name]
        result = collection.update_many(query, {'$set': update})
        return result.modified_count

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count

    def delete_many(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_many(query)
        return result.deleted_count

    def close_connection(self):
        self.client.close()
