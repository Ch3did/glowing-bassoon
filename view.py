import controller as cnt
import model as db
import os
import time





start = cnt.check_password()
if start == True:
    db.start_database()
    while True:
        os.system("clear")
        time.sleep(1)
        print ("####################################")
        print ("--------------PassWD----------------")
        print ("####################################")  
        print("\n") 
        option = cnt.choise()    
        if option not in ['c','r','u','d','e']:
            print("Opção Inválida!!!") 
        if option=="c":
            status = db.create()
            if status True:
                print("Deu certo...")
            else: 
                
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



