from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

client= pymongo.MongoClient(os.environ['MONGO_URI'],serverSelectionTimeoutMS=5000)

try:
     db=client["Kawai-app"]
except:
    print("Unable to connect to the server.")
