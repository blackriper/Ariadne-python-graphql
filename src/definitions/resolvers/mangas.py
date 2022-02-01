from config.database import db
from bson import ObjectId

def getMangas(obj,info):
    mangas=db.Mangas.find()
    list_mangas=[]
    for manga in mangas:
        list_mangas.append(manga)
    return list_mangas    

def getManga(*_,id):
   manga=db.Mangas.find_one({"_id":ObjectId(id)})
   return manga    