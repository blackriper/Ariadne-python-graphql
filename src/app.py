from msilib import schema
from ariadne import  make_executable_schema
from ariadne.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
from config import type_defs,conexion_mongodb
from definitions import mutation_kawai,query_kawai,my_format_error


conexion_mongodb()
schema= make_executable_schema(type_defs,[query_kawai,mutation_kawai])

#borrar linea error formater para visulizar errores detallados durante el desarrollo y escribir debug=True
app=CORSMiddleware(GraphQL(schema,error_formatter=my_format_error),
                          allow_origins=['*'],
                          allow_methods=("GET", "POST", "OPTIONS"))


