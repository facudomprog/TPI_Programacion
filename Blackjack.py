import random
import time

def blackjack():
    global cartas,dealer,jugador,valor_dealer,valor_jugador,b
    j=""
    while j != "3":
        print("BIENVENIDO AL BLACKJACK")
        print("1.Empezar a jugar \n2.Como se juega \n3.Salir")
        j=input("Ingresa (1,2,3): ")
        if j == "1":
            while j=="1":
                cartas=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
                dealer=[]
                jugador=[]
                valor_jugador=0
                valor_dealer=0
                b=0
                repartir()
                j=""
                while j!="1" and j!="3":
                    print("1.Jugar otra vez \n2.Salir")
                    j=input("Ingresa (1,2): ")
                    if j =="2":
                        j="3"
                    elif j !="1":
                        print("Ingresaste un numero incorrecto. vuelve a intetarlo")
                        time.sleep(1)
        elif j=="2":
            instrucciones()
            time.sleep(1)
        elif j!="2" and j!="3":
            print("Ingresaste un numero incorrecto. vuelve a intetarlo")
            time.sleep(1)

def repartir():
    global b
    print("Mezclando mazo...")
    time.sleep(1)
    print("Repartiendo cartas...")
    time.sleep(1)
    jugador.append(cartas[random.randint(0,len(cartas)-1)])
    print("🎴 Blackjack 🎴")
    print("🃏-------------------------------🃏")
    print(f"🂠 Dealer: {dealer} ")
    print("🃏-------------------------------🃏")
    print(f"🂡 Jugador: {jugador} ")
    print("🃏-------------------------------🃏")
    print("Repartiendo cartas...")
    time.sleep(2)
    dealer.append(cartas[random.randint(0,len(cartas)-1)])
    print("🎴 Blackjack 🎴")
    print("🃏-------------------------------🃏")
    print(f"🂠 Dealer: {dealer} ")
    print("🃏-------------------------------🃏")
    print(f"🂡 Jugador: {jugador} ")
    print("🃏-------------------------------🃏")
    print("Repartiendo cartas...")
    time.sleep(2)
    jugador.append(cartas[random.randint(0,len(cartas)-1)])
    print("🎴 Blackjack 🎴")
    print("🃏-------------------------------🃏")
    print(f"🂠 Dealer: {dealer} ")
    print("🃏-------------------------------🃏")
    print(f"🂡 Jugador: {jugador} ")
    print("🃏-------------------------------🃏")
    print("Repartiendo cartas...")
    time.sleep(2)
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
        print("🎴 Blackjack 🎴")
        print("🃏-------------------------------🃏")
        print(f"🂠 Dealer: {dealer} ({valor_dealer})")
        print("🃏-------------------------------🃏")
        print(f"🂡 Jugador: {jugador} ({valor_jugador})")
        print("🃏-------------------------------🃏")
        resultado()
    elif b != 0:
        mostrar()

def mostrar():
    global b
    orden=""
    print("🎴 Blackjack 🎴")
    print("🃏-------------------------------🃏")
    print(f"🂠 Dealer: {dealer} ({valor_dealer})")
    print("🃏-------------------------------🃏")
    print(f"🂡 Jugador: {jugador} ({valor_jugador})")
    print("🃏-------------------------------🃏")
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
        while orden!="1" and orden!="2":
            orden=input("Ingrese un numero 1 o 2: ")
            if orden == "1":
                pedir(orden)
            elif orden=="2":
                dealer[1]=b
                b=0
                calcular()
            else:
                print("Ingresaste un numero incorrecto. vuelve a intetarlo")
                time.sleep(1)

def pedir(orden):
    if orden=="1":
        jugador.append(cartas[random.randint(0,len(cartas)-1)])
        print("El dealer esta sacando una carta...")
        time.sleep(2)
        calcular()
    elif orden=="2":
        dealer.append(cartas[random.randint(0,len(cartas)-1)])
        print("El dealer esta sacando una carta...")
        time.sleep(2)
        calcular()

def resultado():
    if valor_jugador>21:
        print("PERDISTE")
    elif valor_dealer>21:
        print("GANASTE")
    elif valor_jugador==21 and len(jugador)==2 and valor_dealer==21 and len(dealer)==2:
                print("EMPATE")
    elif valor_jugador==21 and len(jugador)==2:
                print("GANASTE")
    elif valor_dealer==21 and len(dealer)==2:
                print("PERDISTE")
    elif valor_dealer<=16:
        pedir("2")
        return
    elif valor_dealer > valor_jugador:
        print("PERDISTE")
    elif valor_jugador> valor_dealer:
        print("GANASTE")
    elif valor_dealer==valor_jugador:
        print("EMPATE")
    time.sleep(1)

def instrucciones():
    print("""
    -------------------------------------------
    **Objetivo del juego:**
    El objetivo es conseguir una mano con un valor total lo más cercano posible a 21, sin pasarse.
    **Cómo jugar:**
    1. **Valor de las cartas:**
    - Las cartas del 2 al 10 valen su número.
    - Las figuras (J, Q, K) valen 10.
    - El As vale 1 o 11, según lo que más te convenga.
    2. **Inicio del juego:**
    - Tú (el jugador) y el dealer (la casa) reciben 2 cartas cada uno.
    - Solo una carta del dealer se muestra al principio.
    3. **Tus opciones:**
    - **Pedir: Solicitas una carta adicional.
    - **Quedarte: Conservas tu mano actual y termina tu turno.
    4. **El turno del dealer:**
    - El dealer debe pedir cartas hasta tener al menos 17 puntos.
    - Si pasa de 21, pierde automáticamente.
    5. **Cómo ganas:**
    - Ganas si tu mano es 21 o está más cerca de 21 que la del dealer, sin pasarte.
    - Si te pasas de 21, pierdes automáticamente.
    -------------------------------------------
    """)