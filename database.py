import sqlite3

conn = sqlite3.connect('sql_passwd.db')

def start_database():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords(
                    id INTEGER PRIMARY KEY,
                    serv TEXT NOT NULL,
                    user TEXT NOT NULL,
                    pass TEXT NOT NULL);
         ''')

def create():
    c = conn.cursor()
    serv = input("Qual o servico?: ")
    user = input("Qual o user?: ")
    passw = input("Qual o password?: ")
    c.execute(''' INSERT INTO passwords(serv, user, pass)
        VALUES(?,?,?); ''' , (serv, user, passw)) 
    if c.rowcount <= 1:
        print("Deu certo...")
    else:
        print("Deu errado...")
def read():
    pass



def update():
    pass



def delete():
    pass
