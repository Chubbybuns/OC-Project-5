from peewee import *
from secrets import user, password
from entities import Category, Product, Saved_product

mysql_db = MySQLDatabase('oc5', user=user, password=password,
                         host='127.0.0.1', port=3306)


# Category.create(Category_name='Saucisson')

mysql_db.connect()

Saved_product.drop_table()
Product.drop_table()
Category.drop_table()


mysql_db.create_tables([Category, Product, Saved_product])

"""Category.get(Category.id == 1)"""
categories = Category.select()
for category in categories:
    print(category.name)

