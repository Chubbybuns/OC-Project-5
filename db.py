from peewee import MySQLDatabase
from secrets import user, password, db_name, host

mysql_db = MySQLDatabase(db_name, user=user, password=password,
                         host=host, port=3306)
