from peewee import *
from . import BaseModel, Category, Product


class Saved_product(BaseModel):
    id = AutoField(null=True, primary_key=True)
    category_id = ForeignKeyField(Category, backref='Category')
    substitute = ForeignKeyField(Product, backref='Substitute')
    substitued = ForeignKeyField(Product, backref='Substitued')