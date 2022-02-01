from config.database import db
from bson import ObjectId

def newManga(_, info,manga):
     newmanga={
       "title":manga['title'],  
       "cover":manga['cover'],
       "description": manga['description'],
       "genre":manga["genre"],
       "rank":manga['rank'],
       "favorite":False
    }
     id=db.Mangas.insert_one(newmanga).inserted_id
     return "Manga created with id: {}".format(id)
