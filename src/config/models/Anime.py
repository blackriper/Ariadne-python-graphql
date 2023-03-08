from mongoengine import (
    Document,
    StringField,
    IntField,
    ListField,
    DictField,
    BooleanField,
    ReferenceField
)
from .helper import mongo_to_dict

class Anime(Document):
    title = StringField(required=True)
    cover = StringField(required=True)
    description = StringField(required=True)
    type = StringField(required=True, default="anime")
    genre = ListField(StringField(), required=True)
    rank = StringField(required=True)
    favorite = BooleanField(default=False)
    chapters = IntField(default=0)
    sequel=ListField(ReferenceField('self'))
    prequels=ListField(ReferenceField('self'))
    meta={'collection':'Animes'}

    def to_dict(self):
     return mongo_to_dict(self,[]) 