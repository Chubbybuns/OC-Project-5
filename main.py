import os
import time
from sys import exit
from entities import Category, Product, Saved_product

categories = Category.select()


def welcome_message():
    # os.system('cls')
    print("Bienvenue dans l'application qui transformera votre assiette.")
    print("Veuillez choisir la catégorie de l'aliment que vous voulez substituer dans la liste ci-dessous.")
    display_categories()


def display_categories():
    count = 0
    for category in categories:
        count += 1
        print(f"{count}. {category.name}")
    print("\nEntrez 'Q' pour quitter")
    choose_category()


def choose_category():
    choice = input("Quel est votre choix ? ")
    if choice.lower() == 'q':
        exit(0)
    possible_choices = [i for i in range(1, len(categories)+1)]
    number = int(choice)
    if number in possible_choices:
        display_products_from_category(number)
    else:
        print(f"Veuillez choisir un nombre entre {len(categories) - (len(categories) - 1 )} et {len(categories)}.")
        choose_category()


def display_products_from_category(number):
    category = Category.get_by_id(number)
    products = Product.select().where(Product.category_id == number)
    count = 0
    print(f"Vous avez choisi {category.name}.")
    time.sleep(1)
    print("Veuillez choisir l'aliment que vous voulez substituer dans la liste ci-dessous.")
    for product in products:
        count += 1
        print(f"{count}. {product.name}")
    print("\nEntrez 'Q' pour quitter")
    choose_product()


def choose_product(number):
    products = Product.select().where(Product.category_id == number)
    possible_choices = [i for i in range(1, len(products) + 1)]
    choice = input("Quel est votre choix ? ")
    if choice.lower() == 'q':
        exit(0)
    number = int(choice)
    if number in possible_choices:
        get_substitute(number)
    else:
        print(f"Veuillez choisir un nombre entre {len(products) - (len(products) - 1 )} et {len(products)}.")
        choose_product(number)


def get_substitute(number):
    substitued_product = Product.select().where()
    substitute_product = Product.select().where(Product.nutriscore > substitued_product.nutriscore)
    print(f"Je vous propose de substituer {substitued_product.name} par {substitute_product.name}")
    choice = input("Voulez-vous sauvegarder ce produit ? O/N")
    if choice == "O":
        print("Produit sauvegardé")
    if choice == "N":
        print("Produit non sauvegardé")
        product = Saved_product(category_id=number,
                                substitute=substitute_product.id,
                                substitued=substitued_product.id)
        product.save()
    elif choice.lower()=="q":
        exit(0)
    else:
        print("Veuillez entre 'O' ou 'N'")



welcome_message()

