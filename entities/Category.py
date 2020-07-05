from peewee import *
from .BaseModel import BaseModel


class Category(BaseModel):
    id = AutoField(null=True, primary_key=True)
    name = CharField(null=True)
