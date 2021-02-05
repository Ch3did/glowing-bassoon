import sqlite3
import bcrypt 
import controller as cnt

conn = sqlite3.connect('sql_passwd.db')

def check_password():
    #Hash de senha pré definida 
    senha = b'$2b$12$BUcr3KyHcCMb.Pivy3C3V./6NCZuN45RrwoFEs/jEWaUIOf7NySmO'
    kick = cnt.kick()
    if bcrypt.checkpw(kick, senha):
        return True
    else:
        return False

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
    serv, user, passwd = cnt.create_values()
    c.execute(''' INSERT INTO passwords(serv, user, pass)
        VALUES(?,?,?) ''' , (serv, user, passwd)) 
    if c.rowcount <= 1:
        conn.commit()
        return True 
    else:
        return False
    c.close()

def read():
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    rows = c.fetchall()
    return rows

def update():
    c = conn.cursor()
    choose_column= input("'serv', 'user', 'pass'? : ")
    choose_id= input("Qual o ID? : ")
    new_value= input("Qual o novo valor? : ")
    c.execute('''UPDATE passwords
                SET {} = '{}'
                WHERE id  = {};'''.format(choose_column, new_value, int(choose_id)))
    conn.commit()
    c.close()

def delete():
    c= conn.cursor()
    choose_delete= input("Qual o id? : ")
    c.execute('''DELETE FROM passwords
                WHERE id = {};'''.format(choose_delete))
    conn.commit()
    c.close()