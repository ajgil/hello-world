from math import sqrt
from random import random
import sys

bankroll = 0
apuesta = 0
listaApuestas = []
sec = 0
tipoApuesta = False

def apestasApuesta(bankroll,apuesta):
   if (apuesta >= bankroll):
       print ("Eh! apestas a apuesta falsa jaja. No te queda presupuesto... abandona!")
       sys.exit(0)
   return

def winBeneficio(win,beneficio):
    if (win >= beneficio):
        print("Has ganado mucho dineriiiiiitooo")
        sys.exit(0)

print("Hola Roulettero, Bienvenido a apuesta o muere!")
print("Esta app indica la cantidad de iteraciones que necesitas para alcanzar tu objetivo, bribón!")
bankroll = int(input ("Indica tu presupuesto: "))
apuesta = int(input("Indica cantidad a apostar: "))
apestasApuesta(bankroll,apuesta)
beneficio = int (input("¿Cuanto quieres ganar?: "))
#input("Presiona intro")
print("\n")
print("Listado de secuencias de apuestas disponibles:\n----------------------------------")
print("Fibonacci: Obtiene el siguiente número de la serie cuando pierde, resta 2 posiciones cuando gana")
print("Martingala: Dobla la apuesta anterior siempre que hayas perdido, si gana no dobla")
sec = int(input("Elige 1 para Fibonacci o 2 para Martingala: "))
#input("Presiona intro")
#print("\n")
#print("Listado de apuestas:\n--------------------")
#print("Apuesta a números pares escribiendo 'pares'")
#print("Apuesta a números impares escribiendo 'impares'")
#tipoApuesta = input("Escribe 'pares' o 'impares', ¿A qué apuestas?: ")

# Fibonnaci
def F(n):
   #fib = ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
   #print("fibonacci apuesta: ", fib)
   return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

# Martingala
def M(n):
   mart = n*2
   print (mart)
   return mart

# Apuestas rojo, negro, par, impar con el 0 -verde-
def betstowin(bankroll, apuesta, beneficio):
   i = 1
   win = 0
   print("Apuesta\tResultado Aleatorio\tGana/Pierde\t\tBankroll")
      
   while apuesta < bankroll:
        winBeneficio(bankroll,beneficio)
        aleatorio=random()
        if aleatorio<0.45: # Rojo y par ganan
            win=int(apuesta)*2
            bankroll = bankroll + win
            print("{}\t\t{}\t\tGANA\t{}\t\t{}".format(apuesta,str(aleatorio)[0:4],win,bankroll))
        elif aleatorio<0.90: # Negro impar pierden
            loose=int(apuesta)
            bankroll = bankroll - loose 
            print("{}\t\t{}\t\tPIERDE\t{}\t\t{}".format(apuesta,str(aleatorio)[0:4],loose,bankroll))
            apuesta = int(F(apuesta))
            print ("apuesta con fib", apuesta )
        else: # Verde 0 pierde
            loose=int(apuesta)
            bankroll = bankroll - loose
            print("{}\t\t{}\t\tCero - PIERDE\t{}\t\t{}".format(apuesta,str(aleatorio)[0:5],loose,bankroll))
            apuesta = int(apuesta + F(apuesta))
                        
        i=i+1
        #apuesta = int(apuesta + F(apuesta))
        # print("ahora apuesas: ", apuesta)

        if (bankroll <= apuesta):
            print("----- Has perdido todo tu dinero en {} tiradas -------".format(i))
            return
                
   print("-FIN DEL PROGRAMA, HAS NECESITADO {} TIRADAS -".format(i))

#ruleta(10)
#betstowin(bankroll)
betstowin(bankroll,apuesta,beneficio)
