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
    conn.commit()
    c.close()

def create():
    c = conn.cursor()
    serv = input("Qual o servico?: ")
    user = input("Qual o user?: ")
    passw = input("Qual o password?: ")
    c.execute(''' INSERT INTO passwords(serv, user, pass)
        VALUES(?,?,?); ''' , (serv, user, passw)) 
    if c.rowcount <= 1:
        print("Deu certo...")
        conn.commit()
    else:
        print("Deu errado...")
    c.close()



def read():
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    rows = c.fetchall()
    print("--------------------------------------------------------------------------------------------")
    for row in range(len(rows)):
        print("Serviço: {}  | Usuário: {}  | Senha: {}  | ID: {}  ".format(rows[row][1], rows[row][2], rows[row][3], rows[row][0]))
    print("--------------------------------------------------------------------------------------------")