from config import Anime

"""Metodos para obtener los ids  y generar listas para los reference field """

def get_sequel_and_prequels(newanime):
  
   list_prequels=[get_anime(_id) for _id in newanime['prequels']]
   list_sequel=[get_anime(_id)  for _id in newanime['sequel']]

   del newanime['prequels']
   del newanime['sequel']     

   return {
           **newanime,
           "sequel": list_sequel,
           "prequels": list_prequels
           
           }

#actualizar las secuelas de los animea agregados como prequelas
def update_sequel(anime):
   for a in anime.prequels:
       Anime.objects(id=a.id).update_one(push__sequel=anime)          


#obtener un documento anime para secuelas o precuelas
def get_anime(_id):
  return {"anime":an for an in Anime.objects(id=_id)}['anime']


#covertir objecto anime a dict anime
def get_dictAnime(anime):
     return dict(
            _id=str(anime.id),
            title=anime.title,
            cover=anime.cover,
            description=anime.description,
            type=anime.type,
            genre=anime.genre,
            rank=anime.rank,
            favorite=anime.favorite,
            chapters=anime.chapters,
            sequel=[doc.to_dict() for doc in anime.sequel],
            prequels=[doc.to_dict() for doc in anime.prequels]
       )