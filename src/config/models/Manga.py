from mongoengine import (
    Document,
    StringField,
    IntField,
    ListField,
    BooleanField,
)

from .helper import mongo_to_dict


class Manga(Document):
    title = StringField(required=True)
    cover = StringField(required=True)
    description = StringField(required=True)
    type = StringField(required=True, default="manga")
    genre = ListField(StringField(), required=True)
    rank = StringField(required=True)
    favorite = BooleanField(default=False)
    chapters = IntField(default=0)
    meta={'collection':'Mangas'}

    def to_dict(self):
     return mongo_to_dict(self,[]) 

   