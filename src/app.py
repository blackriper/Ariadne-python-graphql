from msilib import schema
from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from definitions.resolvers.animes import getAnimes,getAnime
from definitions.resolvers.mangas import getMangas,getManga
from definitions.resolvers.favorites import getFavorites
from definitions.mutations.animes import newAnime
from definitions.mutations.mangas import newManga
from definitions.mutations.favorites import addFavorite,deleteFavorite
from ariadne import ObjectType
from ariadne import MutationType
from starlette.middleware.cors import CORSMiddleware

#schemas
type_defs= load_schema_from_path("./definitions/schemas/Kawai.graphql")


#resolvers
query_kawai= ObjectType("Query")
query_kawai.set_field("Animes",getAnimes)
query_kawai.set_field("getAnime",getAnime)
query_kawai.set_field("Mangas",getMangas)
query_kawai.set_field("getManga",getManga)
query_kawai.set_field("Favorites",getFavorites)



#muttations
mutation_kawai = MutationType()
mutation_kawai.set_field("newAnime",newAnime)
mutation_kawai.set_field("newManga",newManga)
mutation_kawai.set_field("addFavorite",addFavorite)
mutation_kawai.set_field("deleteFavorite",deleteFavorite)



schema= make_executable_schema(type_defs,[query_kawai,mutation_kawai])

app=CORSMiddleware(GraphQL(schema, debug=True),allow_origins=['*'], allow_methods=("GET", "POST", "OPTIONS"))