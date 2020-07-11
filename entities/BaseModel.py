from peewee import Model, MySQLDatabase
from secrets import user, password

mysql_db = MySQLDatabase('oc5', user=user, password=password,
                         host='127.0.0.1', port=3306)


class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db
