from peewee import *
from secrets import user, password

mysql_db = MySQLDatabase('oc5', user=user, password=password,
                         host='127.0.0.1', port=3306)

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db


class Category(BaseModel):
    id = AutoField(null=True, primary_key=True)
    name = CharField(null=True)


class Product(BaseModel):
    id = AutoField(null=True, primary_key=True)
    category_id = ForeignKeyField(Category, backref='Products')
    name = CharField(null=True)
    description = TextField()
    nutriscore = IntegerField()
    country = CharField()
    store = TextField()
    link = TextField()


class Saved_product(BaseModel):
    id = AutoField(null=True, primary_key=True)
    category_id = ForeignKeyField(Category, backref='Category')
    substitute = ForeignKeyField(Product, backref='Substitute')
    substitued = ForeignKeyField(Product, backref='Substitued')


# Category.create(Category_name='Saucisson')

mysql_db.connect()

Saved_product.drop_table()
Product.drop_table()
Category.drop_table()


mysql_db.create_tables([Category, Product, Saved_product])

data_source = [
    {'name': 'Saucisson'},
    {'name': 'Fromage'},
    {'name': 'Vin'}
]

for data_dict in data_source:
    try:
        Category.create(**data_dict)
    except Exception:
        print("problème données")


"""Category.get(Category.id == 1)"""
categories = Category.select()
for category in categories:
    print(category.name)

