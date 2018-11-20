# -*- coding: utf-8 -*-
from math import sqrt
from random import random
import os
import sys

def apestasApuesta(bankroll,apuesta):
   if (apuesta >= bankroll):
       print ("Eh! apestas a apuesta falsa. No intentes engañarme... abandona!")
       sys.exit(0)
   return

def menu():
    '''
    Limpiamos la pantalla
    '''
    os.system('clear') #Windows cls
    print("Hola Roulettero, Bienvenido a apuesta o muere!")
    print("Esta app indica la cantidad de iteraciones que necesitas para alcanzar tu objetivo, bribón!")   
    #input("Presiona intro")
#listaApuestas = []
#tipoApuesta = False

def ganancias(bankroll,aux2,i):
    if (bankroll >= aux2):
        print("Has conseguido tu objetivo de ganar {} Euros".format(aux2))
        print("Has ganado {}. Eso es mucho dineriiiiiitooo en {} apuestas".format(bankroll,i-1))
        sys.exit(0)

def perdidas(bankroll,apuesta,i):
    if (bankroll <= apuesta):
        print("----- Has perdido todo tu dinero en {} tiradas -------".format(i-1))
        print("----- Te ha quedado un bankroll de {} aurelios -------".format(bankroll))
        sys.exit(0)
        #return

# Fibonnaci
def F(n):
   return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

# Resta 2 posiciones fibonacci
def fibomenosdos(n):
    if n > 2:
        n -= 2
        return int(F(n))
    else:
        return 1

# Martingala
def M(n):
   return n*2

while True:
    # Mostramos menu
    #menu()

    # solicituamos una opción al usuario
    bankroll = int(input ("Indica tu presupuesto: "))
    apinicial = int(input("Indica cantidad a apostar: "))
    apuesta = apinicial
    apestasApuesta(bankroll,apuesta)
    beneficio = int (input("¿Cuanto quieres ganar?: ")) # Cuanto quiero ganar
    print("Listado de series disponibles:\n------------------------------------")
    print("Fibonacci: Cuando pierde obtiene siguiente número, resta 2 posiciones cuando gana")
    print("Martingala: Dobla la apuesta anterior cuando pierde, si gana vuelve a iniciar la secuencia")
    print("Ambas: Comparativa entre ambas secuencias")
    sec = input("Elige: \n 1 para Fibonacci \n 2 para Martingala \n 3 ambas >> ")

    if sec == "1":
        print ("")
        # implementamos fibonacci
        def fib(bankroll, apuesta, beneficio):
            i = 1
            win = 0
            fibo = 1
            aux2 = bankroll + beneficio
            print("tirada\tApuesta\tFibonacci\tGana/Pierde\t\tResultado\tBankroll")
            while apuesta < bankroll:
                ganancias(bankroll,aux2,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    if (fibo == 0 or fibo == 1):
                        apuesta = apinicial # 0
                    elif (fibo == 2):
                        apuesta = apinicial + 1 # 1,1
                    elif (fibo == 3): 
                        apuesta = apinicial + 2 # 2
                    else:
                        apuesta = apinicial + int(F(fibo-2))
                        fibo -= 2
                    win=int(apuesta)
                    bankroll = bankroll + win
                    print("{}\t{}\t{}\t\tGANA\t\t{}\t{}\t\t{}".format(i,apuesta,fibo,win,str(aleatorio)[0:4],bankroll))
                elif aleatorio<0.90: # Negro impar pierden
                    if fibo == 1:
                        apuesta = apinicial
                    else:
                        apuesta = int(F(fibo)) + apinicial
                    loose=int(apuesta)
                    bankroll = bankroll - loose 
                    print("{}\t{}\t{}\t\tPIERDE\t\t{}\t{}\t\t{}".format(i,apuesta,fibo,loose,str(aleatorio)[0:4],bankroll))
                    fibo +=1
                else: # Verde 0 pierde
                    if fibo == 1:
                        apuesta = apinicial
                    else:
                        apuesta = int(F(fibo)) + apinicial
                    loose=int(apuesta)
                    bankroll = bankroll - loose
                    print("{}\t{}\t{}\t\tPIERDE - 0\t{}\t{}\t\t{}".format(i,apuesta,fibo,loose,str(aleatorio)[0:5],bankroll))
                    fibo += 1                
                
                i += 1
                perdidas(bankroll,apuesta,i)
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
                    print("{}\t{}\t\t{}\t\tPIERDE - 0\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:5],loose,bankroll,aux))
                    apuesta *= 2                    
                
                i += 1
                perdidas(bankroll,apuesta,i)

        mart(bankroll, apuesta, beneficio)
    elif sec == "3":
        print("")
        # implementamos fibonacci
        def fib_(bankroll, apuesta, beneficio):
            i = 1
            win = 0
            fibo = 1
            total = bankroll + beneficio
            print("tirada\tApuesta\tResultado Aleatorio\tGana/Pierde\t\tBankroll\tFibonacci")
            while apuesta < bankroll:
                ganancias(bankroll,total,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    win=int(apuesta)
                    bankroll = bankroll + win
                    apuesta = int(F(fibo - 2))
                    if apuesta <= 0:
                        apuesta = 1
                    #print("{}\t{}\t\t{}\t\tGANA\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],win,bankroll,aux))
                    return apuesta,win,bankroll,fibo
                elif aleatorio<0.90: # Negro impar pierden
                    fibo +=1
                    loose=int(apuesta)
                    bankroll = bankroll - loose 
                    apuesta = int(F(fibo))
                    #print("fibonacci {}".format(aux))
                    #print("{}\t{}\t\t{}\t\tPIERDE\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],loose,bankroll,aux))
                    return apuesta, loose, bankroll, fibo
                else: # Verde 0 pierde
                    fibo += 1
                    loose=int(apuesta)
                    bankroll = bankroll - loose
                    apuesta = int(F(fibo))  
                    #print("{}\t{}\t\t{}\t\tCero - PIERDE\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:5],loose,bankroll,aux))
                    return apuesta, loose, bankroll, fibo                   
                
                i += 1
                perdidas(bankroll,apuesta,i)
            return i

        #print(fib_(bankroll, apuesta, beneficio))
    else:
        break
