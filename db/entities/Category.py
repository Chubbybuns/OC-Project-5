from peewee import *
from .BaseModel import BaseModel


class Category(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    url = CharField()
