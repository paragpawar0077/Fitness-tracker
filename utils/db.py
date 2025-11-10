from pymongo import MongoClient
import os
# Connect to MongoDB running locally (default port 27017)
# client = MongoClient("mongodb://localhost:27017/")

# Use environment variable for MongoDB connection (for deployment)
# Falls back to localhost for local development

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
# Create or connect to the database
db = client["fittrack_db"]

# Create or connect to a collection (like a table)
workouts_collection = db["workouts"]
