"""Cambiar el formateador de errores por defecto por 
uno personalizado 
"""
from ariadne import format_error
from graphql import GraphQLError

def my_format_error(error: GraphQLError, debug: bool = False) -> dict:
    if debug:
        # If debug is enabled, reuse Ariadne's formatting logic (not required)
        return format_error(error, debug)

    # Create formatted error data
    formatted = error.formatted
    # Replace original error message with custom one
    formatted["message"] = "INTERNAL SERVER ERROR"
    return formatted
