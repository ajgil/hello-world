# -*- coding: utf-8 -*-
from math import sqrt
from random import random
import os
import sys

def apestasApuesta(bankroll,apuesta):
   if (apuesta >= bankroll):
       print ("Eh! apestas a apuesta falsa jaja. No te queda presupuesto... abandona!")
       sys.exit(0)
   return

def menu():
    '''
    Limpiamos la pantalla
    '''
    os.system('cls') #Linux cls
    print("Hola Roulettero, Bienvenido a apuesta o muere!")
    print("Esta app indica la cantidad de iteraciones que necesitas para alcanzar tu objetivo, bribón!")   
    #input("Presiona intro")
   
#bankroll, apuesta, sec = 0,0,0
#listaApuestas = []
#tipoApuesta = False

def ganancias(bankroll,aux2,i):
    if (bankroll >= aux2):
        print("Has conseguido tu objetivo de ganar {} Euros".format(aux2))
        print("Has ganado {}. Eso es mucho dineriiiiiitooo en {} apuestas".format(bankroll,i-1))
        sys.exit(0)

# Fibonnaci
def F(n):
   #fib = int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
   return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

# Martingala
def M(n):
   return n*2

while True:
    # Mostramos menu
    #menu()

    # solicituamos una opción al usuario
    bankroll = int(input ("Indica tu presupuesto: "))
    apuesta = int(input("Indica cantidad a apostar: "))
    apestasApuesta(bankroll,apuesta)
    beneficio = int (input("¿Cuanto quieres ganar?: ")) # Cuanto quiero ganar
    print("Listado de series / secuencias disponibles:\n----------------------------------")
    print("Fibonacci: Obtiene el siguiente número de la serie cuando pierde, resta 2 posiciones cuando gana")
    print("Martingala: Dobla la apuesta anterior siempre que hayas perdido, si gana vuelve a iniciar la secuencia")
    sec = input("Elige 1 para Fibonacci o 2 para Martingala >> ")

    if sec == "1":
        print ("")
        # implementamos fibonacci
        def fib(bankroll, apuesta, beneficio):
            i = 1
            win = 0
            aux = 1
            aux2 = bankroll + beneficio
            print("tirada\tApuesta\tResultado Aleatorio\tGana/Pierde\t\tBankroll\tFibonacci")
            
            while apuesta < bankroll:
                ganancias(bankroll,aux2,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    win=int(apuesta)
                    bankroll = bankroll + win
                    apuesta = int(F(aux - 2))
                    if apuesta <= 0:
                        apuesta = 1
                    print("{}\t{}\t\t{}\t\tGANA\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],win,bankroll,aux))
                elif aleatorio<0.90: # Negro impar pierden
                    aux +=1
                    loose=int(apuesta)
                    bankroll = bankroll - loose 
                    print("{}\t{}\t\t{}\t\tPIERDE\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],loose,bankroll,aux))
                    apuesta = int(F(aux))
                    #print("fibonacci {}".format(aux))
                else: # Verde 0 pierde
                    aux += 1
                    loose=int(apuesta)
                    bankroll = bankroll - loose
                    print("{}\t{}\t\t{}\t\tCero - PIERDE\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:5],loose,bankroll,aux))
                    apuesta = int(F(aux))                      
                
                
                i += 1

                if (bankroll <= apuesta):
                    print("----- Has perdido todo tu dinero en {} tiradas -------".format(i-1))
                    print("----- Te ha quedado un bankroll de {} aurelios -------".format(bankroll))
                    return
                        
            print("-FIN DEL PROGRAMA, HAS NECESITADO {} TIRADAS -".format(i))
        fib(bankroll, apuesta, beneficio)
    elif sec == "2":
        print("")
        # implementamos martingala
        def mart(bankroll, apuesta, beneficio):
            i = 1
            win = 0
            aux = 1
            aux2 = bankroll + beneficio
            print("tirada\tApuesta\tResultado Aleatorio\tGana/Pierde\t\tBankroll\tMartingala")
            while apuesta < bankroll:
                ganancias(bankroll,aux2,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    win=int(apuesta)
                    bankroll = bankroll + win
                    print("{}\t{}\t\t{}\t\tGANA\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],win,bankroll,aux))
                    apuesta = 1
                elif aleatorio<0.90: # Negro impar pierden
                    loose=int(apuesta)
                    bankroll = bankroll - loose 
                    print("{}\t{}\t\t{}\t\tPIERDE\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],loose,bankroll,aux))
                    apuesta *= 2
                else: # Verde 0 pierde
                    loose=int(apuesta)
                    bankroll = bankroll - loose
                    print("{}\t{}\t\t{}\t\tCero - PIERDE\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:5],loose,bankroll,aux))
                    apuesta *= 2                    
                
                i += 1

                if (bankroll <= apuesta):
                    print("----- Has perdido todo tu dinero en {} tiradas -------".format(i-1))
                    print("----- Te ha quedado un bankroll de {} aurelios -------".format(bankroll))
                    return
                        
            print("-FIN DEL PROGRAMA, HAS NECESITADO {} TIRADAS -".format(i))
        mart(bankroll, apuesta, beneficio)
    else:
        break
