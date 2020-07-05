import requests
from entities import Category
# import Product

NUMBER_OF_CATEGORIES = 10
MINIMUM_OF_PRODUCTS_IN_CATEGORY = 3


def get_categories():

    url = "https://fr.openfoodfacts.org/categories.json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    categories = response.json()
    tags = categories["tags"]
    count = 0
    list_of_categories = {}
    for category in tags:
        if category["products"] > MINIMUM_OF_PRODUCTS_IN_CATEGORY:
            category = Category(name=Category["name"])
            list_of_categories += category
            print(category["name"])
            count += 1
        if count == NUMBER_OF_CATEGORIES:
            break


get_categories()
