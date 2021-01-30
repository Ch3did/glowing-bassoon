import model as db
import security as sec 
import os
import time


def choise():
    choise = str(input("O que quer fazer?: "))
    return choise


start = sec.check_password()
if start == True:
    db.start_database()
    while True:
        os.system("clear")
        time.sleep(1)
        print ("####################################")
        print ("--------------PassWD----------------")
        print ("####################################")  
        print("\n") 
        option = choise()    
        if option not in ['c','r','u','d','e']:
            print("Opção Inválida!!!") 
        if option=="c":
            db.create()
        if option=="r":
            db.read()
        if option=="u":
            db.update()
        if option=="d":
            db.delete()
        if option=="e":
            for i in range (1, 4):
                os.system("clear")
                print ("Exiting sistem... ",i)
                time.sleep(1)
            os.system("clear")
            break

        input("PRESS ENTER TO CONTINUE...")

else:
    print("Wrong password")
    time.sleep(1)
    os.system("clear")
    exit



