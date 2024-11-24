import random
cartas=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
dealer=[]
jugador=[]
valor=0

def repartir():
    jugador.append(cartas[random.randint(0,len(cartas)-1)])
    dealer.append(cartas[random.randint(0,len(cartas)-1)])
    jugador.append(cartas[random.randint(0,len(cartas)-1)])
    b=(cartas[random.randint(0,len(cartas)-1)])
    dealer.append("?")
    calcular()

def calcular():
    global valor
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
            valor = valor+9
        a=a-1
    mostrar()

def mostrar():
    print(f"Dealer: {dealer}")
    print()
    print(f"Jugador: {jugador} ({valor})")
    print("1.Pedir  2.Quedarse")
    orden=int(input("Ingrese un numero 1 o 2: "))
    if orden == 1:
        pedir(orden)
    if orden==2:
        pedir(orden)

def pedir(orden):
    if orden==1:
        jugador.append(cartas[random.randint(0,len(cartas)-1)])
        calcular()
    if orden==2:
        dealer.append(cartas[random.randint(0,len(cartas)-1)])
        calcular()

repartir()