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
# Entradas por teclado
def easy_input(question, answer=None, default=None):
    """Ask a question, return an answer.	
	<question> is a string that is presented to the user.
	<answer> is a list of strings presented as a choice. User may type only first letters
	<default> is the presumed answer if the user just hits <Enter>.
	"""
    if answer is None :
	    answer = ['si', 'no']
    else: 
        answer = [i.lower() for i in answer]
	
    # if <default> is None or <default> is not an expected answers
    # <default> will be the first of the expected answers
    if default is None or default not in answer :
	    default = answer[0]

    prompt = '/'.join([
        "\x1b[1;1m{0}\x1b[1;m".format(i.capitalize()) if i == default else i
        for i in answer
    ])
	
    while True :
        choice = input("{0} [{1}]: ".format(question, prompt)).lower()

        if default is not None and choice == '':
            return default
        if choice in answer :
            return choice

        valid_answer = { i[:len(choice)] : i for i in answer }

        if len(valid_answer) < len(answer) :
            print(" -- Ambiguous, please use a more detailed answer.")
        elif choice in valid_answer :
            return valid_answer[choice]
        else:
            print(" -- Por favor, responda solo {0} or {1}.".format(", ".join(answer[:-1]), answer[-1]))

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
def ganancias_(*args):
    #for v in args:
    #print ('cantidad de argumentos', len(args))
    #print("argumentos como lista:", args)
    if args[0] >= args[1]:
        print("Has conseguido tu objetivo de ganar {} Euros".format(args[1]))
        print("Has ganado {}. Eso es mucho dineriiiiiitooo en {} apuestas".format(args[0],args[2]-1))
        sys.exit(0)

# mirar bankroll por debajo de apuesta y perdidas
def bank_(*args):
    #for v in args:
    #print ('cantidad de argumentos', len(args))
    #print("argumentos como lista:", args)
    if (len(args) == 5):
        if args[0] <= args[1]:
            print("----- Pichon has perdido todo tu dinero en {} tiradas -------".format(args[2]-1))
            print("----- Te ha quedado un bankroll de {} aurelios -------".format(args[0]))
            sys.exit(0)
        if args[3] <= args[4]:
            print("----- Pichon has perdido todo tu dinero en {} tiradas -------".format(args[2]-1))
            print("----- Te ha quedado un bankroll de {} aurelios -------".format(args[0]))
            sys.exit(0)
    else:
        if (args[0] <= 0):
            print("Has perdido todo tu dinero. Tienes un bankroll de {}".format(args[0]))
        elif (args[0] <= args[1]):
            print("lista de argumentos:", args)
            print("La siguiente apuesta es {} y tienes un bankroll de {}".format(args[1],args[0]))
            #reset = input("¿Quieres reiniciar la secuencia de apuestas o terminar? s/n >> ").lower().strip()
            reset = easy_input("¿Quieres reiniciar la secuencia de apuestas o terminar? s/n >> ",['s','n'],'s')
            print('reset: {}'.format(reset))
            if  ( sec == 1) :
                apuesta = apinicial
                fib(args[0],apuesta,args[2])
            elif sec == 2 :
                mart(args[0],apuesta,args[2])
            else:
                print("----- Te ha quedado un bankroll de {} aurelios -------".format(args[0]))
                sys.exit(0)

# Fibonnaci
def F(n):
   return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

# Calc posicion fibonacci. fibo comienza en F(2) = 1
def apfibo(n):
    global fibo
    if (n <= 1):
        ap = apinicial # 0 y 1
        fibo = 2
    else:       
        ap = apinicial + int(F(n-2)) 
    return ap, fibo

while True:
    # Mostramos menu
    # menu()

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
    sec = int (input("Elige: \n 1 para Fibonacci \n 2 para Martingala \n 3 ambas >> "))

    if sec == 1:
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
                bank_(bankroll, apuesta, i-1)
        fib(bankroll, apuesta, beneficio)
    elif sec == 2:
        # implementamos martingala
        print('martingala')
        def mart(bankroll, apuesta, beneficio):
            i = 1
            win = 0
            target = bankroll + beneficio
            print("tirada\tApuesta\tGana/Pierde\t\tResultado\tBankroll")
            while apuesta < bankroll:
                ganancias_(bankroll,target,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    win=int(apuesta)
                    bankroll = bankroll + win
                    print("{}\t{}\tGANA\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],win,bankroll))
                    apuesta = 1
                elif aleatorio<0.90: # Negro impar pierden
                    loose=int(apuesta)
                    bankroll = bankroll - loose 
                    print("{}\t{}\tPIERDE\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],loose,bankroll))
                    apuesta *= 2
                else: # Verde 0 pierde
                    loose=int(apuesta)
                    bankroll = bankroll - loose
                    print("{}\t{}\tPIERDE - 0\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:5],loose,bankroll))                    
                    apuesta *= 2
                i += 1
                bank_(bankroll,apuesta,i)

        mart(bankroll, apuesta, beneficio)
    elif sec == 3:
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
                bank_(martbank,martap,i,fibobank,fiboap)
        martfib(bankroll, apuesta, beneficio)
    else:
        break