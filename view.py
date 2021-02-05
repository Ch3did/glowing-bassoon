import controller as cnt
import model as db
import os
import time

#Constante
opç = ['c','r','u','d','e']

def template():
    os.system("clear")
    print ("####################################")
    print ("--------------PassWD----------------")
    print ("####################################")  
    print("\n")

if db.check_password() == True:
    db.start_database()
    while True:
        template() 
        option = cnt.choise() 
        if option not in opç:
            print("Opção Inválida!!!") 

        #Create ----------------------------------------------------------
        if option=="c":
            status = db.create()
            if status == True:
                print("Deu certo...")
            else: 
                print("Deu Ruim...")

        #Read ------------------------------------------------------------
        if option=="r":
            rows = db.read()
            print("--------------------------------------------------------------------------------------------")
            for row in range(len(rows)):
                print("Serviço: {}  | Usuário: {}  | Senha: {}  | ID: {}  ".format(rows[row][1], rows[row][2], rows[row][3], rows[row][0]))
                print("--------------------------------------------------------------------------------------------")
        
        #Update ------------------------------------------------------------
        if option=="u":
            status = db.update()
            if status <= 1:
                print("Atualização Feita com sucesso") 
            else:
                print("Falha na alteração")
    
    
        #Delete -----------------------------------------------------------
        if option=="d":
            db.delete()
        
        #Exit ------------------------------------------------------------            
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



        