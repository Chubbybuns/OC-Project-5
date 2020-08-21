from flask import Flask, request, Response
from entities import Category, Product, Saved_product
from playhouse.shortcuts import model_to_dict
import random
import json


# TODO : Ycréer db.py + import dans db initialisation
# TODO : YAPI_request --> populate_database.py
# TODO : Ynouvelle syntaxe pour les réponses --> fonction return_json()
# TODO : Yretourner directement une liste au lieu d'un dictionnaire
# TODO : YDate time en json serializable
# TODO : Base de données sur free.fr ? --> plus rapide
# TODO : Heroku: mettre API
# TODO : modifier main.py avec les endpoints de l'api


app = Flask(__name__)


def response_as_json(data):
    response = app.response_class(
        response=json.dumps(data, indent=4, sort_keys=True, default=str),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/")
def hello():
    return "Yo"


@app.route('/api/categories/', methods=["GET"])
def get_categories():
    categories = Category.select()
    categories_as_dict = list(categories.dicts())
    return response_as_json({"categories": categories_as_dict})


@app.route('/api/categories/<int:category_id>/products', methods=["GET"])
def get_products_from_category(category_id):
    category_id_exists = Category.select().where(Category.id == category_id).get()
    if category_id_exists is not None:
        products_from_category = Product.select().where(Product.category_id == category_id)
        print(products_from_category)
        dict_of_products = list(products_from_category.dicts())
        return response_as_json(dict_of_products)
    return Response("incorrect category id", status=404)


@app.route('/api/categories/<int:category_id>/products/<int:product_id>', methods=["GET"])
def get_substitute(category_id, product_id):
    category_id_exists = Category.select().where(Category.id == category_id).get()
    product_id_exists = Product.select().where(Product.id == product_id).get()
    if category_id_exists is not None and product_id_exists is not None:
        substitued_product = Product.select().where(Product.id == product_id).get()
        potential_subsitute_products = Product.select().where(
            (Product.category_id == category_id) &
            (Product.nutriscore < substitued_product.nutriscore))
        if len(potential_subsitute_products) == 0:
            return Response("Could not find a substitute product", status=400)
        substitute_product = random.choice(potential_subsitute_products)
        return response_as_json({"substitute": model_to_dict(substitute_product)})
    elif category_id_exists is None and product_id_exists is not None:
        return Response("Incorrect category ID", status=404)
    else:
        return Response("Incorrect product ID", status=404)


@app.route('/api/save_products/', methods=["POST"])
def save_product():
    substitute_product_exists = len(Product.select().where(Product.id == request.form["substitute_product_id"])) == 1
    substitued_product_exists = len(Product.select().where(Product.id == request.form["substitued_product_id"])) == 1
    if substitute_product_exists and substitued_product_exists:
        product = Saved_product(substitute=request.form["substitute_product_id"],
                                substitued=request.form["substitued_product_id"])
        product.save()
        return response_as_json({"saved_product": model_to_dict(product)})
    elif not substitued_product_exists and substitute_product_exists:
        return Response("Substitued product ID does not exist", status=404)
    else:
        return Response("Substitute product ID does not exist", status=404)


@app.route('/api/saved_products/', methods=["GET"])
def get_saved_products():
    saved_products = Saved_product.select()
    saved_products_as_dict = list(saved_products.dicts())
    return response_as_json(saved_products_as_dict)


if __name__ == "__main__":
    app.run(debug=True)
