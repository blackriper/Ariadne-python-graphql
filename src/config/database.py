from dotenv import load_dotenv
from mongoengine import connect
import os

load_dotenv()
db=None

def conexion_mongodb():
     try:
      db=connect(host=os.environ['MONGO_URI'])   
     except:
      print("Unable to connect to the server.")
