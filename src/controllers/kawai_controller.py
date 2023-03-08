from config import Manga,Anime
from .utlis import  (get_sequel_and_prequels,
                     update_sequel,
                     get_dictAnime)

"""Operaciones de mangas"""

def create_Manga(newmanga):
  if(Manga.objects(title=newmanga['title']).count() > 0):
      return f"Manga {newmanga['title']} it already exists"

  manga=Manga(**newmanga).save()
  return f"Manga created with id: {manga.id}"


def favorite_manga(id,val,message):
  Manga(id=id).update(set__favorite=val)
  return f"{id} {message}"


def find_one_manga(id):
  return {"manga": manga.to_dict() for manga in Manga.objects(id=id)}['manga'] 

  
def find_all_manga():
  return[manga.to_dict() for manga in Manga.objects]  

def favorites_manga():
  return[manga.to_dict() for manga in Manga.objects(favorite=True)]

def find_genre_by_manga(genre):
  return[manga.to_dict() for manga in Manga.objects(genre=genre)] 



"""Operaciones para animes"""  

def create_Anime(newanime):
   if(Anime.objects(title=newanime['title']).count() > 0):
       return f"Anime {newanime['title']} it already exists"
 
   anime=Anime(**get_sequel_and_prequels(newanime)).save()
   update_sequel(anime)
   return f"Anime created with id: {anime.id}"   


def find_all_anime():
   return [ get_dictAnime(anime) for anime in Anime.objects] 


def find_one_anime(id):
  return {"anime":get_dictAnime(anime) for anime in Anime.objects(id=id)}['anime']


def favorite_anime(id,val,message):
  Anime(id=id).update(set__favorite=val)
  return f"{id} {message}"


def favorites_anime():
  return[get_dictAnime(anime) for anime in Anime.objects(favorite=True)]


def find_genre_by_anime(genre):
  return[get_dictAnime(anime) for anime in Anime.objects(genre=genre)]  