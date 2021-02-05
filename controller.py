import getpass


def choise():
    choise = str(input("O que quer fazer?: "))
    return choise


def create_values():
    serv = input("Qual o servico?: ")
    user = input("Qual o user?: ")
    passw = getpass.getpass("Qual o password?: ")
    return serv, user, passw

def kick():
    kick = bytes(getpass.getpass("? :"), 'utf-8')
    return kick