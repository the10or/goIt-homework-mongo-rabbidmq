from mongoengine import *


class Author(Document):
    fullname = StringField(unique=True)
    born_date = StringField(max_length=30)
    born_location = StringField(max_length=50)
    description = StringField()
    meta = {'collection': 'authors'}


class Quote(Document):
    tags = ListField(StringField(max_length=15))
    author = ReferenceField(Author)
    quote = StringField()
    meta = {'collection': 'quotes'}
