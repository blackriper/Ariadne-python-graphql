from ariadne import MutationType
from controllers import (
                          create_Manga,
                          favorite_manga,
                          create_Anime,
                          favorite_anime)


mutation_kawai = MutationType()


@mutation_kawai.field("newAnime")
def newAnime(_, info,anime):
    return create_Anime(anime)


@mutation_kawai.field("newManga")
def newManga(_, info,manga):
    return create_Manga(manga)
     


@mutation_kawai.field("addFavorite")
def addFavorite(*_,id,classi):
    if classi=="MANGA":
       return favorite_manga(id,True," Manga add favorites")
    
    if classi=="ANIME":
         return favorite_anime(id,True," Anime add favorites")


@mutation_kawai.field("deleteFavorite")
def deleteFavorite(*_,id,classi):
    if classi=="MANGA":
        return favorite_manga(id,False," Manga delete favorites")
       
    if classi=="ANIME":
        return favorite_anime(id,False," Anime delete favorites")
    