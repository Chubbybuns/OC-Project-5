from peewee import *
from . import BaseModel, Category


class Product(BaseModel):
    id = AutoField(null=True, primary_key=True)
    category_id = ForeignKeyField(Category, backref='Products')
    name = CharField(null=True)
    description = TextField()
    nutriscore = IntegerField()
    country = CharField()
    store = TextField()
    link = TextField()
