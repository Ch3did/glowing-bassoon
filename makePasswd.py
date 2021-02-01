import bcrypt

passwd = bytes(input("? :"),'utf-8')
#passws = byte(passwd,'utf-8')
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)
print(hashed)
