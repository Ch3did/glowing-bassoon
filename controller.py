



def choise():
    choise = str(input("O que quer fazer?: "))
    return choise


def create_values():
    serv = input("Qual o servico?: ")
    user = input("Qual o user?: ")
    passw = input("Qual o password?: ")
    print(type(passw))
    return serv, user, passw

def kick():
    kick = bytes(input("? :"), 'utf-8')
    return kick