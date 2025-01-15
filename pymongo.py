import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["db"]
collection = db["pymongo"]

# Define the document to insert
document = {"name": "krish", "age": 20}

try:
    # Insert the document
    result = collection.insert_one(document) 
    print(f"Document inserted with ID: {result.inserted_id}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    client.close()