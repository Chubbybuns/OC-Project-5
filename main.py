import os
import time
import keyboard
import sys


categories = {1: "Saucisson",
              2: "Fromage",
              3: "Vin"}


def welcome_message():
    # os.system('cls')
    print("Bienvenue dans l'application qui transformera votre assiette.")
    print("Veuillez choisir la catégorie de l'aliment que vous voulez substituer dans la liste ci-dessous.")

    for number, item in categories.items():
        print(f"{number}.{item}")
    choose_category()


def choose_category():
    choice = input("Quel est votre choix ? ")
    """if isinstance(choice, int):
        number = int(choice)
    string = str(choice)
    print(type(choice))"""
    number = int(choice) # Pourquoi mettre int ?
    # possible_choices = [1, 2, 3]
    possible_choices = [i for i in range(1, len(categories)+1)] # pourquoi mettre +1 ?
    if number in possible_choices:
        choose_product(number)
    elif choice == 'q': # 'q' n'est pas un int
        sys.exit()
    else:
        print(f"Veuillez choisir un nombre entre {len(categories) - (len(categories) - 1 )} et {len(categories)}.")
        choose_category()
    print(possible_choices)


def choose_product(n):
    print(f"Vous avez choisi {categories[n]}.")


welcome_message()

