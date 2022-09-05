import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def header():
    print("***************************")
    print("**** Caixa Eletrônico *****")
    print("***************************")
