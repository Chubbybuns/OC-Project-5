from peewee import MySQLDatabase
# from secrets import user, password, db_name, host
import os
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
db_name = os.environ.get("DB_NAME")
host = os.environ.get("HOST")

mysql_db = MySQLDatabase(db_name, user=user, password=password,
                         host=host, port=3306)
