from ariadne import ObjectType
from config.database import db
from controllers import (find_one_manga,
                         find_all_manga,
                         find_all_anime,
                         find_one_anime,
                         favorites_anime,
                         favorites_manga,
                         find_genre_by_anime,
                         find_genre_by_manga)

query_kawai= ObjectType("Query")

@query_kawai.field("Animes")
def getAnimes(obj,info):
   return find_all_anime()


@query_kawai.field("getAnime")
def getAnime(*_,id):
   return find_one_anime(id)

@query_kawai.field("Mangas")
def getMangas(obj,info):
     return find_all_manga()


@query_kawai.field("getManga")
def getManga(*_,id):
   return find_one_manga(id)


@query_kawai.field("Favsanime")
def favsanime(obj,info):
   return favorites_anime()

@query_kawai.field("Favsmanga")
def favsanime(obj,info):
   return favorites_manga()   

@query_kawai.field("Genreanime")
def genreanime(*_,genre):
    return find_genre_by_anime(genre)


@query_kawai.field("Genremanga")
def genreanime(*_,genre):
    return find_genre_by_manga(genre)