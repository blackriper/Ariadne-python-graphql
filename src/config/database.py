from dotenv import load_dotenv
from mongoengine import connect
import os

load_dotenv()


def conexion_mongodb():
     try:
      connect(host=os.environ['MONGO_URI'])
     except:
      print("Unable to connect to the server.")
