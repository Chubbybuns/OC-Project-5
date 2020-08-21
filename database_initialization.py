from entities import Category, Product, Saved_product
from db import mysql_db

mysql_db.connect()

Saved_product.drop_table()
Product.drop_table()
Category.drop_table()

mysql_db.create_tables([Category, Product, Saved_product])
