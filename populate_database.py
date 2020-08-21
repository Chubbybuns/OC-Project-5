import requests
from entities import Category, Product


NUMBER_OF_CATEGORIES = 20
MINIMUM_OF_PRODUCTS_IN_CATEGORY = 5
NUMBER_OF_PRODUCTS = 10


def get_categories_and_products():

    url_categories = "https://fr.openfoodfacts.org/categories.json"
    response = requests.request("GET", url_categories)
    categories = response.json()
    tags = categories["tags"]
    count = 0
    list_of_categories = []
    for c in tags:
        if c["products"] > MINIMUM_OF_PRODUCTS_IN_CATEGORY:
            category = Category(name=c["name"], url=c["url"])
            category.save()
            list_of_categories.append(category)
            print(c["name"])
            count += 1
        if count == NUMBER_OF_CATEGORIES:
            break

    for category in list_of_categories:
        url_category = category.url + ".json"
        response = requests.request("GET", url_category)
        products = response.json()
        products = products["products"]
        list_of_products = []
        count = 0
        for p in products:
            if not all(tag in p for tag in ("product_name", "ingredients_text", "nutrition_grades", "countries",
                                            "stores", "url")):
                pass
            else:
                product = Product(category_id=category.id,
                                  name=p["product_name"],
                                  description=p["ingredients_text"],
                                  nutriscore=p["nutrition_grades"],
                                  country=p['countries'],
                                  store=p["stores"],
                                  link=p['url'])
                product.save()
                list_of_products.append(product)
                count += 1
                print(p["product_name"])
            if count == NUMBER_OF_PRODUCTS:
                break


get_categories_and_products()
