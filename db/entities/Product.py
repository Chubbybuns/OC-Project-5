from peewee import *
from .BaseModel import BaseModel
from .Category import Category


class Product(BaseModel):
    id = AutoField(primary_key=True)
    category_id = ForeignKeyField(Category, backref='Products')
    name = CharField()
    description = TextField()
    nutriscore = CharField()
    country = CharField()
    store = TextField(null=True)
    link = TextField()

    def __str__(self):
        return self.name + "(" + self.nutriscore + ")"
