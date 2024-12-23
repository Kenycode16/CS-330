from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        """Initialize the MongoClient to access MongoDB."""
        # MongoDB Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33749
        DB = 'AAC'
        COL = 'animals'

        # Use authSource=admin to authenticate against the admin database
        connection_string = f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin'

        try:
            # Establish the MongoDB connection
            self.client = MongoClient(connection_string)
            self.database = self.client[DB]
            self.collection = self.database[COL]
            print("MongoDB connection established successfully.")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")

    def create(self, data):
        """Insert a document into the database."""
        try:
            if data:
                print(f"Attempting to insert: {data}")
                result = self.collection.insert_one(data)
                print(f"Insert result: {result.acknowledged}")
                return result.acknowledged  # Returns True if successful
            else:
                raise ValueError("Data parameter is empty.")
        except Exception as e:
            print(f"An error occurred in create: {e}")
            return False

    def read(self, query):
        """Retrieve documents from the database."""
        try:
            print(f"Querying with: {query}")
            results = self.collection.find(query)
            return [doc for doc in results]  # Convert cursor to a list of documents
        except Exception as e:
            print(f"An error occurred in read: {e}")
            return []
    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print(f"Error updating documents: {e}")
            return 0
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting documents: {e}")
            return 0