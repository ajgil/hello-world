# -*- coding: utf-8 -*-
from math import sqrt
from random import random
import os
import sys

# Variables globales
fibo = 1
apinicial = 0

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

# Calcular emolumentos
'''
def ganancias(bankroll,target,i):
    if (bankroll >= target):
        print("Has conseguido tu objetivo de ganar {} Euros".format(target))
        print("Has ganado {}. Eso es mucho dineriiiiiitooo en {} apuestas".format(bankroll,i-1))
        sys.exit(0)
'''
def ganancias_(*args):
    #for v in args:
    print ('cantidad de argumentos', len(args))
    print("argumentos como lista:", args)
    if args[0] >= args[1]:
        print("Has conseguido tu objetivo de ganar {} Euros".format(args[1]))
        print("Has ganado {}. Eso es mucho dineriiiiiitooo en {} apuestas".format(args[0],args[2]-1))
        sys.exit(0)


# Calcular perdidas
def perdidas_(*args):
    #for v in args:
    print ('cantidad de argumentos', len(args))
    print("argumentos como lista:", args)
    '''if args[0] <= args[1]:
        print("----- Pichon has perdido todo tu dinero en {} tiradas -------".format(args[2]-1))
        print("----- Te ha quedado un bankroll de {} aurelios -------".format(args[0]))
        sys.exit(0)
    if args[3] <= args[4]:
        print("----- Pichon has perdido todo tu dinero en {} tiradas -------".format(args[2]-1))
        print("----- Te ha quedado un bankroll de {} aurelios -------".format(args[0]))
        sys.exit(0)
    '''
    return
# Fibonnaci
def F(n):
   return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

# Calcular posiciones fibonacci
def apfibo(n):
    global fibo
    if (n <= 1):
        ap = apinicial # 0 y 1
        fibo = 1
    else:       
        ap = apinicial + int(F(n-2)) 
    return ap, fibo

while True:
    # Mostramos menu
    menu()

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
        # implementamos fibonacci
        def fib(bankroll, apuesta, beneficio):
            global fibo
            i = 1
            win = 0
            target = bankroll + beneficio
            print("Tirada\tFibo\tApuesta\tGana/Pierde\t\tResultado\tBankroll")
            while apuesta < bankroll:
                ganancias_(bankroll,target,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    apuesta, fibo = apfibo(fibo)
                    win=int(apuesta)
                    bankroll = bankroll + win
                    print("{}\t{}\t{}\tGANA\t\t{}\t{}\t\t{}".format(i,fibo,apuesta,str(aleatorio)[0:4],win,bankroll))
                    fibo -= 2
                elif aleatorio<0.90: # Negro impar pierden
                    apuesta, fibo = apfibo(fibo)
                    loose=int(apuesta)
                    bankroll = bankroll - loose 
                    print("{}\t{}\t{}\tPIERDE\t\t{}\t{}\t\t{}".format(i,fibo,apuesta,str(aleatorio)[0:4],loose,bankroll))
                    fibo +=1
                else: # Verde 0 pierde
                    apuesta, fibo = apfibo(fibo)
                    loose=int(apuesta)
                    bankroll = bankroll - loose
                    print("{}\t{}\t{}\tPIERDE - 0\t{}\t{}\t\t{}".format(i,fibo,apuesta,str(aleatorio)[0:5],loose,bankroll))
                    fibo += 1                
                
                i += 1
                perdidas_(bankroll, apuesta, i-1)
        fib(bankroll, apuesta, beneficio)
    elif sec == "2":
        # implementamos martingala
        def mart(bankroll, apuesta, beneficio):
            i = 1
            win = 0
            target = bankroll + beneficio
            print("tirada\tMartin\tApuesta\tGana/Pierde\t\tResultado\tBankroll")
            while apuesta < bankroll:
                ganancias_(bankroll,target,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    win=int(apuesta)
                    bankroll = bankroll + win
                    apuesta, martin = 1,1
                    print("{}\t{}\t\t{}\t\tGANA\t\t{}\t{}\t\t{}".format(i,martin,apuesta,str(aleatorio)[0:4],win,bankroll))
                elif aleatorio<0.90: # Negro impar pierden
                    loose=int(apuesta)
                    bankroll = bankroll - loose 
                    apuesta *= 2
                    martin *= 2
                    print("{}\t{}\t\t{}\t\tPIERDE\t\t{}\t{}\t\t{}".format(i,martin,apuesta,str(aleatorio)[0:4],loose,bankroll))
                else: # Verde 0 pierde
                    loose=int(apuesta)
                    bankroll = bankroll - loose
                    apuesta *= 2
                    martin *= 2
                    print("{}\t{}\t\t{}\t\tPIERDE - 0\t{}\t{}\t\t{}".format(i,martin,apuesta,str(aleatorio)[0:5],loose,bankroll))                    
                
                i += 1
                perdidas_(bankroll,apuesta,i)

        mart(bankroll, apuesta, beneficio)
    elif sec == "3":
        print("")
        # implementamos fibonacci
        def martfib(bankroll, apuesta, beneficio):
            global fibo
            i = 1
            martwin, fibowin = 0,0
            martloose, fiboloose = 0,0
            martap = apuesta
            mart = 1
            martbank = bankroll
            fibobank = bankroll
            target = bankroll + beneficio
            print("tirada\tMartin\tFibo\tMarAp\tFibAp\tGana/Pierde\tMartinRes\tFiboRes\tMartinBank\tFiboBank")
            while apuesta < bankroll:
                ganancias_(bankroll,target,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    martap, mart = 1,1
                    fiboap, fibo = apfibo(fibo)
                    martwin = int(martap)
                    fibowin = int(fiboap)
                    martbank = martbank + martwin
                    fibobank = fibobank + fibowin
                    print("{}\t{}\t{}\t{}\t{}\tGANA {}\t{}\t\t{}\t{}\t\t{}".format(i,mart,fibo,martap,fiboap,str(aleatorio)[0:4],martwin,fibowin,martbank,fibobank))
                    fibo -= 2
                    #return apuesta,win,bankroll,fibo
                elif aleatorio<0.90: # Negro impar pierden
                    fiboap, fibo = apfibo(fibo)
                    martloose = int(martap)
                    fiboloose = int(fiboap)
                    martbank = martbank - martloose
                    fibobank = fibobank - fiboloose
                    print("{}\t{}\t{}\t{}\t{}\tPIERDE {}\t{}\t\t{}\t{}\t\t{}".format(i,mart,fibo,martap,fiboap,str(aleatorio)[0:4],martwin,fibowin,martbank,fibobank))
                    fibo +=1
                    mart *= 2
                    martap *= 2
                else: # Verde 0 pierde
                    fiboap, fibo = apfibo(fibo)
                    martloose = int(martap)
                    fiboloose = int(fiboap)
                    martbank = martbank - martloose
                    fibobank = fibobank - fiboloose
                    print("{}\t{}\t{}\t{}\t{}\tPIERDE {}\t{}\t\t{}\t{}\t\t{}".format(i,mart,fibo,martap,fiboap,str(aleatorio)[0:4],martwin,fibowin,martbank,fibobank))
                    fibo +=1
                    mart *= 2
                    martap *= 2                 
                
                i += 1
                perdidas_(martbank,martap,i,fibobank,fiboap)
        martfib(bankroll, apuesta, beneficio)
    else:
        break
