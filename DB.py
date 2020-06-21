from peewee import *

mysql_db = MySQLDatabase('oc5', user='root', password='93wnxbcv',
                         host='127.0.0.1', port=3306)

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db

class User(BaseModel):
    username = CharField()hy
