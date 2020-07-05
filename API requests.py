import requests
#import Category
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
    for category in tags:
        if category["products"] > MINIMUM_OF_PRODUCTS_IN_CATEGORY:
            print(category["name"])
            count += 1
        if count == NUMBER_OF_CATEGORIES:
            break

            # category = Category(name=category["name"])


get_categories()
