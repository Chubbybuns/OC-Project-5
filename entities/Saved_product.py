from peewee import *
from .BaseModel import BaseModel
from .Category import Category
from .Product import Product


class Saved_product(BaseModel):
    id = AutoField(primary_key=True)
    category_id = ForeignKeyField(Category, backref='Category')
    substitute = ForeignKeyField(Product, backref='Substitute')
    substitued = ForeignKeyField(Product, backref='Substitued')
