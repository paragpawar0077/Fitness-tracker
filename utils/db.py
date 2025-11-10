from pymongo import MongoClient

# Connect to MongoDB running locally (default port 27017)
client = MongoClient("mongodb://localhost:27017/")

# Create or connect to the database
db = client["fittrack_db"]

# Create or connect to a collection (like a table)
workouts_collection = db["workouts"]
