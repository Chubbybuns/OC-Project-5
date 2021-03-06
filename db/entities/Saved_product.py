from peewee import *
from .BaseModel import BaseModel
from .Product import Product
import datetime


class Saved_product(BaseModel):
    id = AutoField(primary_key=True)
    substitute = ForeignKeyField(Product, backref='Substitute')
    substitued = ForeignKeyField(Product, backref='Substitued')
    date = DateTimeField(default=datetime.datetime.now)
