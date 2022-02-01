from ariadne import ObjectType
from config.database import db
from bson import ObjectId

def addFavorite(*_,id,classi):
    if classi=="MANGA":
        db.Mangas.update_one({"_id":ObjectId(id)},{"$set":{"favorite":True}})
        return f"{id} Manga add favorites"
    
    if classi=="ANIME":
         db.Animes.update_one({"_id":ObjectId(id)},{"$set":{"favorite":True}})
         return f"{id} Manga add favorites"


def deleteFavorite(*_,id,classi):
    if classi=="MANGA":
        db.Mangas.update_one({"_id":ObjectId(id)},{"$set":{"favorite":False}})
        return f"{id} Manga delete favorites"
    
    if classi=="ANIME":
         db.Animes.update_one({"_id":ObjectId(id)},{"$set":{"favorite":False}})
         return f"{id} Anime delete favorites"
    