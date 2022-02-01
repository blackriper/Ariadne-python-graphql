from config.database import db
from bson import ObjectId

def getAnimes(obj,info):
    col=db.Animes.find()
    list_animes=[]
    for anime in col:
        list_animes.append(anime)
    return list_animes



def getAnime(*_,id):
   anime=db.Animes.find_one({"_id":ObjectId(id)})
   return anime