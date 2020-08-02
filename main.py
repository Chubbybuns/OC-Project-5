import time
from sys import exit
from entities import Category, Product, Saved_product
import random


class NotANumberError(Exception):
    pass


class NumberNotInRangeError(Exception):
    pass


categories = Category.select()
saved_products = Saved_product.select()


def welcome_message():
    print("Bienvenue dans l'application qui transformera votre assiette.")


def view_saved_products():

    for saved_product in saved_products:
        print(f"You substitued {saved_product.substitued.name} with {saved_product.substitute.name}")


def display_categories():
    print("Veuillez choisir la catégorie de l'aliment que vous voulez substituer dans la liste ci-dessous.")
    count = 0
    for category in categories:
        count += 1
        print(f"{count}. {category.name}")
    print("\nEntrez 'Q' pour quitter \nPour voir les produits de substitution enregistrés, entrez 'V'")


def choose_first_option():
    possible_choices = [i for i in range(1, len(categories) + 1)]
    choice = input("Quel est votre choix ? ")
    if choice.lower() == 'q':
        exit(0)
    elif choice.lower() == 'v':
        view_saved_products()
        return None
    else:
        # Si l'input n'est pas un nombre
        try:
            number = int(choice)
        except ValueError:
            print(f"Veuillez choisir un nombre entre {len(categories) - (len(categories) - 1)} et {len(categories)}.")
            raise NotANumberError()

        if number not in possible_choices:
            # Si l'input est un nombre hors fourchette
            print(f"Veuillez choisir un nombre entre {len(categories) - (len(categories) - 1)} et {len(categories)}.")
            raise NumberNotInRangeError()

        return number


def get_products_from_category(number):
    category = Category.get_by_id(number)
    products = Product.select().where(Product.category_id == number)
    number_of_products = products.count()
    return category, products, number_of_products


def display_products_from_category(category, products, number_of_products):
    print(f"\n\nVous avez choisi {category.name}. Il y a {number_of_products} produits dans {category.name}.")
    time.sleep(1)
    print("\n\nVeuillez choisir l'aliment que vous voulez substituer dans la liste ci-dessous.")
    count = 0
    for product in products:
        count += 1
        print(f"{count}. {product.name}")
    print("\nEntrez 'Q' pour quitter")


def choose_product(category_id):
    products = Product.select().where(Product.category_id == category_id)
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


def get_substitute(category_id, substitued_product):
    # select un random produit parmi les produits restants de la catégorie
    potential_subsitute_products = Product.select().where(
        (Product.category_id == category_id) &
        (Product.nutriscore < substitued_product.nutriscore)
    )
    try:
        substitute_product = random.choice(potential_subsitute_products)
    except IndexError:
        return None
    return substitute_product
    # print toutes les caractéristiques du substitut


def display_substitute(substitute_product, substitued_product, number):
    print(f"Je vous propose de substituer {substitued_product.name} par {substitute_product.name}")
    choice = input("Voulez-vous sauvegarder ce produit ? O/N")
    if choice.lower() == "O":
        print("Produit sauvegardé")
    elif choice.lower() == "N":
        print("Produit non sauvegardé")
        product = Saved_product(category_id=number,
                                substitute=substitute_product.id,
                                substitued=substitued_product.id)
        product.save()
    elif choice.lower() == "q":
        exit(0)
    else:
        print("Veuillez entre 'O' ou 'N'")


def main():
    welcome_message()
    while True:
        display_categories()

        try:
            number = choose_first_option()
        except NotANumberError:
            number = choose_first_option()
        except NumberNotInRangeError:
            number = choose_first_option()

        if number is not None:
            category, products, number_of_products = get_products_from_category(number)
            display_products_from_category(category, products, number_of_products)
            product = choose_product(category.id)
            substitute_product = get_substitute(category.id, product)
            if substitute_product is None:
                print("Je n'ai pas trouvé de produit de substitution. Désolé. :^(")
            else:
                display_substitute(substitute_product, product, category.id)


main()

