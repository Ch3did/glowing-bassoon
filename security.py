import bcrypt

def check_password():
    #Hash de senha pré definida 
    senha = b'$2b$12$BUcr3KyHcCMb.Pivy3C3V./6NCZuN45RrwoFEs/jEWaUIOf7NySmO'
    kick = bytes(input("? :"), 'utf-8')
    hashed = bcrypt.hashpw(kick,bcrypt.gensalt())
    if bcrypt.checkpw(kick, senha):
        return True
    else:
        return False



 