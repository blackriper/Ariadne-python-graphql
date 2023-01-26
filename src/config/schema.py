
#import schema for graphql to python
from ariadne import load_schema_from_path

type_defs= load_schema_from_path("config/schema")