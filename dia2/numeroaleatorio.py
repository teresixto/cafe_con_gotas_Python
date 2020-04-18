#!/usr/bin/env python

from random import randint

def validar(entrada):
    
    try:
        x = int(entrada)
    except ValueError as identifier:
        print ("Debe ser un número entre 0 e 100")
        return False
    except Exception as e:
        print ("Error desconocido")
        return False 
    if ((int(entrada) < 0) or (int(entrada) > 100)):
        print ("O numero debe estar entre 0 e 100")
        return False
    
    return True 

def main():
    busqueda = randint(0,100)
   
    intentos = 0
    jugar = True
    while jugar:
        intentos = intentos + 1
        entrada = input("Escribe algo:")
        print("Ha tecleado: " + entrada)
        validar (entrada)

        if int(entrada) > busqueda:
            print("Su numero esta por está por encima del premiado")
        elif int(entrada) < busqueda:
            print("Su numero esta por debajo por encima del premiado")
        else :
            print("ACERTADO en " + str(intentos) + " intentos") 
            intentos = 0
            volver_xogar = input("Queres volver a xogar: [S/N]")
            if (volver_xogar in ['S','s']):
                jugar = True
                busqueda = randint(0,100)
            else:
                jugar = False
            

    print("Ha finalizado el juego en " + str(intentos) + " intentos.")

if __name__=="__main__":
    main()
    

