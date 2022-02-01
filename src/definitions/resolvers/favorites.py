from config.database import db

def getFavorites(*_,classi):
    list_favorites=[]
    if classi=="MANGA":
     col=db.Mangas.find({"favorite":True})   
     for manga in col:
        list_favorites.append(manga)
     return list_favorites

    if classi=="ANIME":
     col=db.Animes.find({"favorite":True})   
     for anime in col:
        list_favorites.append(anime)
     return list_favorites 

