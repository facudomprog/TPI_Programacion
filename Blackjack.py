import random
import time

cartas=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
dealer=[]
jugador=[]
valor_jugador=0
valor_dealer=0
b=0
def repartir():
    global b
    jugador.append(cartas[random.randint(0,len(cartas)-1)])
    print("-------------------------------------")
    print(f"Dealer: {dealer} ")
    print("-------------------------------------")
    print(f"Jugador: {jugador} ")
    print("-------------------------------------")
    print("Repartiendo cartas")
    time.sleep(3)
    dealer.append(cartas[random.randint(0,len(cartas)-1)])
    print("-------------------------------------")
    print(f"Dealer: {dealer} ")
    print("-------------------------------------")
    print(f"Jugador: {jugador} ")
    print("-------------------------------------")
    print("Repartiendo cartas")
    time.sleep(3)
    jugador.append(cartas[random.randint(0,len(cartas)-1)])
    print("-------------------------------------")
    print(f"Dealer: {dealer} ")
    print("-------------------------------------")
    print(f"Jugador: {jugador} ")
    print("-------------------------------------")
    print("Repartiendo cartas")
    time.sleep(3)
    b=(cartas[random.randint(0,len(cartas)-1)])
    dealer.append("?")
    calcular()

def calcular():
    global valor_jugador, valor_dealer
    valor=0
    a=0
    for i in jugador:
        match i:
            case "2":
                valor+=2
            case "3":
                valor+=3
            case "4":
                valor+=4
            case "5":
                valor+=5
            case "6":
                valor+=6
            case "7":
                valor+=7
            case "8":
                valor+=8
            case "9":
                valor+=9
            case "10":
                valor+=10
            case "J":
                valor+=10
            case "Q":
                valor+=10
            case "K":
                valor+=10
            case "A":
                valor+=1
                a+=1
    while a>0:
        if valor<=12:
            valor = valor+10
        a=a-1
    valor_jugador=valor
    valor=0
    a=0
    for i in dealer:
        match i:
            case "2":
                valor+=2
            case "3":
                valor+=3
            case "4":
                valor+=4
            case "5":
                valor+=5
            case "6":
                valor+=6
            case "7":
                valor+=7
            case "8":
                valor+=8
            case "9":
                valor+=9
            case "10":
                valor+=10
            case "J":
                valor+=10
            case "Q":
                valor+=10
            case "K":
                valor+=10
            case "A":
                valor+=1
                a+=1
    while a>0:
        if valor<=12:
            valor = valor+10
        a=a-1
    valor_dealer=valor
    if b == 0:
        print("-------------------------------------")
        print(f"Dealer: {dealer} ({valor_dealer})")
        print("-------------------------------------")
        print(f"Jugador: {jugador} ({valor_jugador})")
        print("-------------------------------------")
        resultado()
    elif b != 0:
        mostrar()

def mostrar():
    global b
    orden=0
    print("-------------------------------------")
    print(f"Dealer: {dealer} ({valor_dealer})")
    print("-------------------------------------")
    print(f"Jugador: {jugador} ({valor_jugador})")
    print("-------------------------------------")
    if valor_jugador>21:
        dealer[1]=b
        b=0
        calcular()
    elif valor_jugador==21 and len(jugador)==2:
        dealer[1]=b
        b=0
        calcular()
    else:
        print("1.Pedir  2.Quedarse")
        while orden!=1 or orden!=2:
            try:
                orden=int(input("Ingrese un numero 1 o 2: "))
                if orden == 1:
                    pedir(orden)
                    break
                elif orden==2:
                    dealer[1]=b
                    b=0
                    calcular()
                    break
            except: ValueError
            print("Ingresaste un numero incorrecto. vuelve a intetarlo")

def pedir(orden):
    if orden==1:
        jugador.append(cartas[random.randint(0,len(cartas)-1)])
        print("El dealer esta sacando una carta...")
        time.sleep(3)
        calcular()
    elif orden==2:
        dealer.append(cartas[random.randint(0,len(cartas)-1)])
        print("El dealer esta sacando una carta...")
        time.sleep(3)
        calcular()

def resultado():
    if valor_jugador>21:
        print("Perdiste 1")
    elif valor_dealer>21:
        print("GANASTE 2")
    elif valor_dealer<=16:
        pedir(2)
    elif valor_jugador==21 and len(jugador)==2 and valor_dealer==21 and len(dealer)==2:
                print("EMPATE 3")
    elif valor_jugador==21 and len(jugador)==2:
                print("GANASTE 4")
    elif valor_dealer==21 and len(dealer)==2:
                print("PERDISTE 5")
    elif valor_dealer > valor_jugador:
        print("PERDISTE 6")
    elif valor_jugador> valor_dealer:
        print("GANASTE 7")
    elif valor_dealer==valor_jugador:
        print("EMPATE 8")

repartir()