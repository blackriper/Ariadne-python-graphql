from config.database import db
from bson import ObjectId

def newAnime(_, info,anime):
     newanime={
       "title":anime['title'],  
       "cover":anime['cover'],
       "description": anime['description'],
       "genre":anime["genre"],
       "rank":anime['rank'],
       "favorite":False
    }
     id=db.Animes.insert_one(newanime).inserted_id
     return "Anime created with id: {}".format(id)

  

