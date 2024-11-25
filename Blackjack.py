import random
import time

def blackjack():
    global cartas,dealer,jugador,valor_dealer,valor_jugador,b
    j=""
    while j != "3":
        print("🂡🂱🂲🎴 ¡BIENVENIDO AL BLACKJACK! 🎴🂡🂱🂲") # Menú Principal.
        print("🃏-----------------------------------🃏")
        print("1. Empezar a jugar")
        print("2. Instrucciones")
        print("3. Salir")
        print("🃏-----------------------------------🃏")
        j=input("👉 Ingresa tu opción (1, 2 o 3): ")
        if j == "1":
            while j=="1":
                cartas=["2","3","4","5","6","7","8","9","10","J","Q","K","A"] # Inicializacion de variables.
                dealer=[]
                jugador=[]
                valor_jugador=0
                valor_dealer=0
                b=0
                repartir()
                j=""
                print("🔁 ¿Qué quieres hacer ahora? 🔁") # Se muestra despues de terminar la partida.
                print("🃏-----------------------------------🃏")
                print("1. Jugar otra vez")
                print("2. Menú Principal")
                print("3. Salir")
                print("🃏-----------------------------------🃏")
                while j!="1" and j!="3" and j!="0":
                    j = input("👉 Ingresa tu opción (1, 2 o 3): ")
                    if j =="2":
                        j="0"
                    elif j !="1" and j!="3":
                        print("⚠️ Oops! Ingresaste un número incorrecto. ⚠️")
                        print("💡 Por favor, intenta nuevamente con un número válido (1, 2 o 3).")
                        time.sleep(1)
        elif j=="2":
            instrucciones()
            time.sleep(1)
        elif j!="2" and j!="3":
            print("⚠️ Oops! Ingresaste un número incorrecto. ⚠️")
            print("💡 Por favor, intenta nuevamente con un número válido (1, 2 o 3).")
            time.sleep(1)
    print("\n🎉 GRACIAS POR JUGAR 🎉")
    time.sleep(1.5)

def repartir(): # Reparto de cartas.
    global b
    print("\n🔄 Mezclando mazo...")
    time.sleep(1)
    print("🎴 Repartiendo cartas...")
    time.sleep(1)
    jugador.append(cartas[random.randint(0,len(cartas)-1)])
    print("🎴 Blackjack 🎴")
    print("🃏------------------------------------------🃏")
    print(f"🂠 Dealer: {dealer} ")
    print("🃏------------------------------------------🃏")
    print(f"🂡 Jugador: {jugador} ")
    print("🃏------------------------------------------🃏")
    print("🎴 Repartiendo cartas...")
    time.sleep(2)
    dealer.append(cartas[random.randint(0,len(cartas)-1)])
    print("🎴 Blackjack 🎴")
    print("🃏------------------------------------------🃏")
    print(f"🂠 Dealer: {dealer} ")
    print("🃏------------------------------------------🃏")
    print(f"🂡 Jugador: {jugador} ")
    print("🃏------------------------------------------🃏")
    print("🎴 Repartiendo cartas...")
    time.sleep(2)
    jugador.append(cartas[random.randint(0,len(cartas)-1)])
    print("🎴 Blackjack 🎴")
    print("🃏------------------------------------------🃏")
    print(f"🂠 Dealer: {dealer} ")
    print("🃏------------------------------------------🃏")
    print(f"🂡 Jugador: {jugador} ")
    print("🃏------------------------------------------🃏")
    print("🎴 Repartiendo cartas...")
    time.sleep(2)
    b=(cartas[random.randint(0,len(cartas)-1)])
    dealer.append("?")
    calcular()

def calcular():
    global valor_jugador, valor_dealer,b
    valor=0
    a=0
    for i in jugador: # Calcula los puntos de el jugardor.
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
        if valor<=11:
            valor = valor+10
        a=a-1
    valor_jugador=valor
    valor=0
    a=0
    for i in dealer: # Calcula los puntos del dealer.
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
        if valor<=11:
            valor = valor+10
        a=a-1
    valor_dealer=valor
    if b == 0: # Muestra la carta oculta del dealer, cuando el jugador tiene >=21 o se planta.
        print("🎴 Blackjack 🎴")
        print("🃏------------------------------------------🃏")
        print(f"🂠 Dealer: {dealer} ({valor_dealer})")
        print("🃏------------------------------------------🃏")
        print(f"🂡 Jugador: {jugador} ({valor_jugador})")
        print("🃏------------------------------------------🃏")
        resultado()
    elif valor_jugador>=21:
        dealer[1]=b
        b=0
        calcular()
    elif b != 0:
        mostrar()

def mostrar(): # Muestra ambas manos y su valor.
    global b
    orden=""
    print("🎴 Blackjack 🎴")
    print("🃏------------------------------------------🃏")
    print(f"🂠 Dealer: {dealer} ({valor_dealer})")
    print("🃏------------------------------------------🃏")
    print(f"🂡 Jugador: {jugador} ({valor_jugador})")
    print("🃏------------------------------------------🃏")
    if valor_jugador==21 and len(jugador)==2: # Entra si el jugador saca 21 con 2 cartas.
        dealer[1]=b
        b=0
        calcular()
    else: # Le pide una orden al jugador.
        time.sleep(2)
        print("┌──────────────────────────────┐")
        print("│    ¿Qué deseas hacer?        │")
        print("├──────────────────────────────┤")
        print("│  1. Pedir otra carta         │")
        print("│  2. Quedarte con tu mano     │")
        print("└──────────────────────────────┘")
        while orden!="1" and orden!="2":
            orden=input("👉 Ingresa tu opción (1 o 2): ")
            if orden == "1":
                pedir(orden)
            elif orden=="2":
                dealer[1]=b
                b=0
                calcular()
            else:
                print("⚠️ Oops! Ingresaste un número incorrecto. ⚠️")
                print("💡 Por favor, intenta nuevamente con un número válido (1 o 2).")
                time.sleep(1)

def pedir(orden): # Le da una carta al jugador o al dealer.
    if orden=="1":
        jugador.append(cartas[random.randint(0,len(cartas)-1)])
        print("🎴 El dealer está sacando una carta para ti... 🎴")
        time.sleep(2)
        print("🔄 Calculando tu nueva mano...")
        time.sleep(1)
        calcular()
    elif orden=="2":
        dealer.append(cartas[random.randint(0,len(cartas)-1)])
        print("🃏 El dealer está sacando una carta... 🃏")
        time.sleep(2)
        print("🔄 Calculando la mano del dealer...")
        time.sleep(1)
        calcular()

def resultado(): # Evalua todas las condiciones para terminar el juego.
    if valor_jugador>21:
        time.sleep(1)
        print("PERDISTE (Te pasaste de 21 puntos)😞")
    elif valor_dealer>21:
        time.sleep(1)
        print("GANASTE (El dealer se paso de 21 puntos)🎉")
    elif valor_jugador==21 and len(jugador)==2 and valor_dealer==21 and len(dealer)==2:
                time.sleep(1)
                print("EMPATE (Ambos tienen BLACKJACK)🤝")
    elif valor_jugador==21 and len(jugador)==2:
                time.sleep(1)
                print("GANASTE (Tienes BLACKJACK)🏆")
    elif valor_dealer==21 and len(dealer)==2:
                time.sleep(1)
                print("PERDISTE (El dealer tiene BLACKJACK)😢")
    elif valor_dealer<=16:
        time.sleep(1)
        pedir("2")
        return
    elif valor_dealer > valor_jugador:
        time.sleep(1)
        print("PERDISTE (El dealer tiene mas puntos)😔")
    elif valor_jugador> valor_dealer:
        time.sleep(1)
        print("GANASTE (Tienes mas puntos que el dealer)✨")
    elif valor_dealer ==valor_jugador:
        time.sleep(1)
        print("EMPATE (Ambos tienen los mismos puntos)🤷‍♂️")
    time.sleep(1.5)

def instrucciones(): # Reglas basicas del juego.
    print("""
    🎴--------------------------------------------🎴
    🌟 **Objetivo del juego:** 🌟
    El objetivo es conseguir una mano con un valor total lo más cercano posible a 21, sin pasarse.

    🎯 **Cómo jugar:** 🎯

    1. **Valor de las cartas:**
    - Las cartas del 2 al 10 valen su número.
    - Las figuras (J, Q, K) valen 10.
    - El As vale 1 o 11, según lo que más te convenga.

    2. **Inicio del juego:**
    - Tú (el jugador) y el dealer (la casa) reciben 2 cartas cada uno.
    - Solo una carta del dealer se muestra al principio.

    3. **Tus opciones:**
    - **Pedir:** Solicitas una carta adicional.
    - **Quedarte:** Conservas tu mano actual y termina tu turno.

    4. **El turno del dealer:**
    - El dealer debe pedir cartas hasta tener al menos 17 puntos.
    - Si pasa de 21, pierde automáticamente.

    5. **Cómo ganas:**
    - Ganas si tu mano es 21 o está más cerca de 21 que la del dealer, sin pasarte.
    - Si te pasas de 21, pierdes automáticamente.
    
    🎴--------------------------------------------🎴
    """)