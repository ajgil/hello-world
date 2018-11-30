# -*- coding: utf-8 -*-
from math import sqrt
from random import random
import os
import sys

# Variables globales
fibo = 2
apinicial = 0
tirada = 0

def apestasApuesta(n,a):
   if (a >= n):
       print ("Eh! apestas a apuesta falsa. No intentes engañarme... abandona!")
       sys.exit(0)

#listaApuestas = []
#tipoApuesta = False

# Calcular emolumentos
def ganancias_(*args):
    global beneficio
    global budget
    target = beneficio + budget
    #print("presupuesto {} a ganar {} un total de {}".format(budget,beneficio,target))
    #print("argumentos:", args)
    if len(args) == 1 :    
        if args[0] >= target:
            print("\n Has ganado un total de {} Euros en {} jugadas".format(args[0],args[1]-1))
            sys.exit(0)
    else:
        if args[0] >= target:
            print("\n Has ganado un total de {} Euros en {} jugadas mediante MARTINGALA".format(args[0],args[2]-1))
            sys.exit(0)
        elif args[1] >= target:
            print("\n Has ganado un total de {} Euros en {} jugadas mediante FIBONACCI".format(args[1],args[2]-1))
            sys.exit(0)
        else:
            return

# mirar bankroll por debajo de apuesta y perdidas
def bank_(*args):
    global apinicial
    tirada = args[2]
    if len(args) == 3 :
        bankroll = args[1]
        if args[1] <= 0 :
            print("Has perdido en {} tiradas. Bankroll de {}".format(args[2],args[1]))
            sys.exit(0)
        if args[1] < apinicial :
            print("Tu bankroll {} es menor que la apuesta inicial {}. Bye bye!".format(args[1],apinicial))
            sys.exit(0)       
        if args[0] >= args[1] :
            #print("lista de argumentos:", args)
            print("\nLa siguiente apuesta es {} y tienes un bankroll de {}".format(args[0],args[1]))
            reset = str(input("\n¿Quieres reiniciar la secuencia de apuestas a {} o terminar? s/n \n>> ".format(apinicial))).lower().strip()
            if  ( reset == str('s') and sec == 1 ):
                fib(apinicial, bankroll, tirada)
            elif ( reset == str('s') and sec == 2 ):
                mart(apinicial, bankroll, tirada)
            else:
                print('Ciao bello')
                print('Resumen: bankroll: {} - apuesta {}'.format(args[1],args[0]))
                sys.exit(0)
    elif len(args) == 5 :
        martbank = args[1]
        fibobank = args[4]
        if ( args[1] <= 0 ) :
            print("\nUsando MARTINGALA has perdido en {} tiradas. Bankroll de {}".format(tirada,args[1]))
            sys.exit(1)
        elif args[1] < apinicial :
            print("\nMartingalo, tu bankroll {} es menor que la apuesta inicial {}. Bye bye!".format(args[1],apinicial))
            sys.exit(0)  
        elif (args[4] <= 0 ):
            print("\nUsando FIBONACCI has perdido en {} tiradas. Bankroll de {}".format(tirada,args[4]))
            sys.exit(1)
        elif args[4] < apinicial :
            print("\nFibbi, tu bankroll {} es menor que la apuesta inicial {}. Bye bye!".format(args[4],apinicial))
            sys.exit(0)      
        elif args[0] >= args[1] :
            #print("lista de argumentos:", args)
            print("\nMartingala estás palmando, tu siguiente apuesta es {} y tienes un bankroll de {}".format(args[0],args[1]))
            reset = str(input("\n¿Quieres reiniciar la secuencia de apuestas a {} o terminar? s/n \n>> ".format(apinicial))).lower().strip()
            if reset == str('s') :
                martfibo(apinicial, martbank, tirada, args[3],args[4])
            elif reset == str('n'):
                print('Ciao bello')
                print('Resumen Martingala: bankroll: {} - tirada {}'.format(args[1],args[2]-1))
            else:
                print('No me vaciles!')
                return
        elif args[3] >= args[4] :
            print("\nFibbi estás palmando, tu siguiente apuesta es {} y tienes un bankroll de {} \n".format(args[3],args[4]))
            reset = str(input("\n¿Quieres reiniciar la secuencia de apuestas a {} o terminar? si / no \n>> ".format(apinicial))).lower().strip()
            #reset = easy_input("¿Quieres reiniciar la secuencia de apuestas o terminar? s/n >> ",['s','n'],'s')
            if reset == str('s'):
                fibo = 2
                martfibo(args[0], args[1], tirada, apinicial,fibobank, fibo)
            elif reset == str('n'):
                print('Ciao bello')
                print('Resumen Fibonacci: bankroll: {} - tirada {}'.format(args[4],args[2]-1))
                exit
            else:
                print('No me vaciles!')
                return
        else:
            #print('Ciao bello')
            #print('Resumen Martingalo: bankroll: {} - apuesta {}'.format(args[1],args[0]))
            #print('Resumen Fibbi: bankroll: {} - apuesta {}'.format(args[4],args[3]))
            #sys.exit(0) 
            return

# Fibonnaci
def F(n):
   return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

# Calc posicion fibonacci. fibo comienza en F(2) = 1
def apfibo(n):
    global fibo
    if (n < 3):
        ap = apinicial # [0:3]
        fibo = 2
    else:       
        ap = apinicial + int(F(n)) 
        #print('apuesta inicial {} + fibonacci {}'.format(apinicial,F(n-2)))
    return ap, fibo

while True:
    # Mostramos menu
    # menu()
    budget = int(input ("Indica tu presupuesto: "))
    apinicial = int(input("Indica cantidad a apostar: "))
    apestasApuesta(budget,apinicial)
    beneficio = int (input("¿Cuanto quieres ganar?: ")) # Cuanto quiero ganar
    print("Listado de series disponibles:\n------------------------------------")
    print("Fibonacci: Cuando pierde obtiene siguiente número, resta 2 posiciones cuando gana")
    print("Martingala: Dobla la apuesta anterior cuando pierde, si gana vuelve a iniciar la secuencia")
    print("Ambas: Comparativa entre ambas secuencias")
    sec = int (input("Elige: \n 1 para Fibonacci \n 2 para Martingala \n 3 ambas \n >> "))

    if ( sec == 1 ):
        def fib(*args):
            if args[2] == 0:
                global fibo
                apuesta = args[0]
                bankroll = args[1] # presupuesto es el bankroll
                i = 1
                win = 0
                #print("inicial: fibo {} - ap {} - bankroll {} - tirada {}".format(fibo,apuesta,bankroll,i))
            else:
                apuesta = args[0]
                bankroll = args[1]
                i = args[2]
                fibo = 2
                #print ("regreso de bank: fibo {} - ap {} - bankroll {} - tirada {}".format(fibo,apuesta,bankroll,i))
            print("Tirada\tFibo\tApuesta\tGana/Pierde\t\tResultado\tBankroll")
            while apuesta <= bankroll:
                ganancias_(bankroll,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    win=int(apuesta)
                    bankroll = bankroll + win
                    print("{}\t{}\t{}\tGANA\t\t{}\t{}\t\t{}".format(i,fibo,apuesta,str(aleatorio)[0:4],win,bankroll))
                    fibo -= 2
                    apuesta, fibo = apfibo(fibo)
                elif aleatorio<0.90: # Negro impar pierden
                    loose=int(apuesta)
                    bankroll = bankroll - loose 
                    print("{}\t{}\t{}\tPIERDE\t\t{}\t{}\t\t{}".format(i,fibo,apuesta,str(aleatorio)[0:4],loose,bankroll))
                    fibo +=1
                    apuesta, fibo = apfibo(fibo)
                else: # Verde 0 pierde
                    loose=int(apuesta)
                    bankroll = bankroll - loose
                    print("{}\t{}\t{}\tPIERDE - 0\t{}\t{}\t\t{}".format(i,fibo,apuesta,str(aleatorio)[0:5],loose,bankroll))
                    fibo += 1                
                    apuesta, fibo = apfibo(fibo)
                i += 1
                bank_(apuesta,bankroll,i)
        fib(apinicial, budget, tirada)
    elif ( sec == 2 ):
        def mart(*args):
            if args[2] == 0:
                apuesta = args[0]
                bankroll = args[1]
                i = 1
                win = 0
                #print("inicial: ap {} - bankroll {} - tirada {}".format(apuesta,bankroll,i))
            else:
                apuesta = args[0]
                bankroll = args[1]
                i = args[2]
                #print ("regreso de bank con los argumentos {} - {} - {}".format(apuesta,bankroll, i))
            print("tirada\tApuesta\tGana/Pierde\t\tResultado\tBankroll")
            while apuesta <= bankroll:
                ganancias_(bankroll,i)
                aleatorio=random()
                if aleatorio<0.45: # Rojo y par ganan
                    win=int(apuesta)
                    bankroll = bankroll + win
                    print("{}\t{}\tGANA\t\t{}\t{}\t\t{}".format(i,apuesta,str(aleatorio)[0:4],win,bankroll))
                    apuesta = apinicial
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
                bank_(apuesta,bankroll,i)
        mart(apinicial, budget, tirada)
    elif ( sec == 3 ):
        def martfibo(*args):
            global fibo
            #print("Calculando ambos métodos")
            if len(args) == 3 and args[2] == 0: # tirada inicial
                martap, fiboap = args[0], args[0]
                martbank, fibobank = args[1], args[1]
                i = 1
                martwin, fibowin = 0, 0
                #print("inicial: ap {} - {} - bankroll {} - {} - tirada {}".format(martap,fiboap,martbank,fibobank,i))
            elif len(args) == 5:
                martap = args[0]
                martbank = args[1]
                i = args[2]
                fiboap = args[3]
                fibobank = args[4]
                #print ("argumentos regreso: {} - {} / {} - {} / {}".format(martap, fiboap, martbank, fibobank, i))
            else:
                martap = args[0]
                martbank = args[1]
                i = args[2]
                fiboap = args[3]
                fibobank = args[4]
                fibo = args[5]
                #print ("argumentos regreso: {} - {} / {} - {} / {} / {}".format(martap, fiboap, martbank, fibobank, i, fibo))
            print("tirada\tMartAp\tFiboAp\tGana/Pierde\tResultado\tMartBank\tFibBank")
            while (martap <= martbank or fiboap <= fibobank):
                ganancias_(martbank,fibobank,i)
                aleatorio = random()
                if aleatorio<0.45: # Rojo y par ganan
                    martwin = int(martap)
                    fibowin = int(fiboap)
                    martbank = martbank + martwin
                    fibobank = fibobank + fibowin
                    print("{}\t{}\t{}\tGANA\t{}\t{}\t{}\t{}\t\t{}".format(i,martap,fiboap,str(aleatorio)[0:4],martwin,fibowin,martbank,fibobank))
                    martap = apinicial
                    fibo -= 2
                    fiboap, fibo = apfibo(fibo)
                elif aleatorio<0.90: # Negro impar pierden
                    martloose = int(martap)
                    fiboloose = int(fiboap)
                    martbank = martbank - martloose
                    fibobank = fibobank - fiboloose
                    print("{}\t{}\t{}\tPIERDE\t{}\t{}\t{}\t{}\t\t{}".format(i,martap,fiboap,str(aleatorio)[0:4],martloose,fiboloose,martbank,fibobank))
                    martap *= 2
                    fibo +=1
                    fiboap, fibo = apfibo(fibo)
                else: # Verde 0 pierde
                    martloose = int(martap)
                    fiboloose = int(fiboap)
                    martbank = martbank - martloose
                    fibobank = fibobank - fiboloose
                    print("{}\t{}\t{}\tCERO-P\t{}\t{}\t{}\t{}\t\t{}".format(i,martap,fiboap,str(aleatorio)[0:4],martloose,fiboloose,martbank,fibobank))
                    martap *= 2
                    fibo +=1
                    fiboap, fibo = apfibo(fibo)
                i += 1
                bank_(martap,martbank,i,fiboap,fibobank)
                
        martfibo(apinicial,budget,tirada)   
    else:
        break
