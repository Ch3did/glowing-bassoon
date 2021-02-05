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


def update_values():
    choose_column= input("'serv', 'user', 'pass'? : ")
    choose_id= input("Qual o ID? : ")
    if choose_column == "pass":
        new_value = getpass.getpass("Qual o novo valor? : ")
    else:
        new_value= input("Qual o novo valor? : ")
    return choose_column , choose_id, new_value