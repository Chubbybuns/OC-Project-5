import time
from sys import exit
from os import system, name
from prettytable import PrettyTable
import requests


# TODO: créer un installateur
# TODO: finir view_saved_products() + trouver objectif projet javascript


class NotANumberError(Exception):
    pass


class NumberNotInRangeError(Exception):
    pass


def get_categories_from_api():
    url_categories = "https://foodapi2020.herokuapp.com/api/categories/"
    response = requests.request("GET", url_categories)
    response_as_json = response.json()
    categories = response_as_json["categories"]
    return categories


def get_saved_products_from_api():
    url_saved_products = "https://foodapi2020.herokuapp.com/api/saved_products/"
    response = requests.request("GET", url_saved_products)
    saved_products = response.json()
    return saved_products


def get_products_from_category_from_api(category_id):
    url_products_from_category = "https://foodapi2020.herokuapp.com/api/categories/" + str(category_id) + "/products"
    response = requests.request("GET", url_products_from_category)
    products_from_category = response.json()
    return products_from_category


def get_substitute_from_api(product_id):
    url_substitute = "https://foodapi2020.herokuapp.com/api/substitute_product/" + str(product_id)
    response = requests.request("GET", url_substitute)
    if response.status_code == 404:
        return None
    response_as_json = response.json()
    substitute = response_as_json["substitute"]
    return substitute


def save_product_to_api(substitued_product_id, substitute_product_id):
    url = "https://foodapi2020.herokuapp.com/api/save_products/"
    payload = {'substitued_product_id': str(substitued_product_id),
               'substitute_product_id': str(substitute_product_id)}
    response = requests.request("POST", url, headers={}, data=payload, files=[])

    print(response.text.encode('utf8'))


def clear():
    if name == 'nt':
        _ = system('cls')


def welcome_message():
    print("Bienvenue dans l'application qui transformera votre assiette.")


def view_saved_products():
    saved_products = get_saved_products_from_api()
    saved_products = saved_products["saved_products_list"]
    saved_products_table = PrettyTable()
    saved_products_table.field_names = ["Substitued product name",
                                        "Substitued product link",
                                        "Substitute product name",
                                        "Substitute link",
                                        "Category",
                                        "Date"]
    for saved_products_pair in saved_products:
        saved_products_table.add_row([saved_products_pair["substitued_name"], saved_products_pair["substitued_link"],
                                      saved_products_pair["substitute_name"], saved_products_pair["substitute_link"],
                                      saved_products_pair["category_name"], saved_products_pair["date"]])

    print(saved_products_table)


def display_categories():
    categories_list = get_categories_from_api()
    print("Veuillez choisir la catégorie de l'aliment que vous voulez substituer dans la liste ci-dessous.")
    count = 0
    for category in categories_list:
        count += 1
        print(f"{count}. {category['name']}")
    print("\nEntrez 'Q' pour quitter \nPour voir les produits de substitution enregistrés, entrez 'V'")


def choose_first_option():
    categories_list = get_categories_from_api()
    possible_choices = [i for i in range(1, len(categories_list) + 1)]
    choice = input("Quel est votre choix ? ")
    if choice.lower() == 'q':
        exit(0)
    elif choice.lower() == 'v':
        view_saved_products()
        #time.sleep(5)
        continue_choice = input("Appuyez sur une touche pour continuer ou sur Q pour quitter")
        if continue_choice.lower() == 'q':
            exit(0)
        return None
    else:
        # Si l'input n'est pas un nombre
        try:
            number = int(choice)
        except ValueError:
            print(f"Veuillez choisir un nombre entre {len(categories_list) - (len(categories_list) - 1)} et "
                  f"{len(categories_list)}.")
            raise NotANumberError()

        if number not in possible_choices:
            # Si l'input est un nombre hors fourchette
            print(f"Veuillez choisir un nombre entre {len(categories_list) - (len(categories_list) - 1)} et "
                  f"{len(categories_list)}.")
            raise NumberNotInRangeError()

        return number


def get_products_from_category(number):
    category_list = get_categories_from_api()
    for category in category_list:
        if category["id"] == number:
            products = get_products_from_category_from_api(number)
            number_of_products = len(products)
            return category, products, number_of_products


def display_products_from_category(category, products, number_of_products):
    category_name = category["name"]
    print(f"\n\nVous avez choisi {category_name}. Il y a {number_of_products} produits dans {category_name}.")
    time.sleep(1)
    print("\n\nVeuillez choisir l'aliment que vous voulez substituer dans la liste ci-dessous.")
    count = 0
    for product in products:
        product_name = product["name"]
        count += 1
        print(f"{count}. {product_name}")
    print("\nEntrez 'Q' pour quitter")


def choose_product(category_id):
    products = get_products_from_category_from_api(category_id)
    possible_choices = [i for i in range(1, len(products) + 1)]
    choice = input("Quel est votre choix ? ")
    if choice.lower() == 'q':
        exit(0)
    try:
        number = int(choice)
    except ValueError:
        print(f"Veuillez choisir un nombre entre {len(products) - (len(products) - 1)} et {len(products)}.")
        product = choose_product(category_id)
        return product
    if number not in possible_choices:
        print(f"Veuillez choisir un nombre entre {len(products) - (len(products) - 1)} et {len(products)}.")
        product = choose_product(category_id)
    else:
        product = products[number - 1]
    return product


def get_substitute(substitued_product_id):
    substitute = get_substitute_from_api(substitued_product_id)
    return substitute


def display_substitute(substitute_product, substitued_product):
    substitued_product_name = substitued_product["name"]
    substitute_product_name = substitute_product["name"]
    print(f"\n\nJe vous propose de substituer {substitued_product_name} par {substitute_product_name} :")
    products_table = PrettyTable()
    products_table.field_names = ["Product name",
                                  "Description",
                                  "Nutriscore",
                                  "Country",
                                  "Link"]

    products_table.add_row([substitued_product_name, substitued_product["description"], substitued_product["nutriscore"],
                            substitued_product["country"], substitued_product["link"]])
    products_table.add_row([substitute_product_name, substitute_product["description"], substitute_product["nutriscore"],
                            substitute_product["country"], substitute_product["link"]])
    print(products_table)
    choice = input("Voulez-vous sauvegarder ce produit ? O/N")
    if choice.lower() == "o":
        save_product_to_api(substitued_product["id"], substitute_product["id"])
        print("Produit sauvegardé !")
        time.sleep(3)
    elif choice.lower() == "n":
        print("Produit non sauvegardé")
        time.sleep(3)
    elif choice.lower() == "q":
        exit(0)
    else:
        print("Veuillez entre 'O' ou 'N'")


def main():
    welcome_message()
    time.sleep(3)
    while True:
        clear()
        display_categories()
        try:
            number = choose_first_option()
        except NotANumberError:
            number = None
            clear()
        except NumberNotInRangeError:
            number = None
            clear()
        if number is not None:
            category, products, number_of_products = get_products_from_category(number)
            display_products_from_category(category, products, number_of_products)
            product = choose_product(category["id"])
            substitute_product = get_substitute(product)
            if substitute_product is None:
                print("Je n'ai pas trouvé de produit de substitution. Désolé. :^(")
                time.sleep(3)
            else:
                display_substitute(substitute_product, product)


main()
