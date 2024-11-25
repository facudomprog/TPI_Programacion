import time
import random
def AdivinaElNumero():
    def explicarReglas():
        print("¡¡¡Bienvenido a Adivina el Numero!!!")
        time.sleep(1)
        print("Voy a elegir un numero entre 1 y 100")
        time.sleep(1)
        print("Tenes 10 intentos para adivinarlo. ¡Buena suerte!")


    def miniMenu(modo):
        if modo == 1:
            print("1: ¡Jugar de nuevo!")
        
        else:
            print("1: ¡Jugar!")

        print("2: Salir")
        
        verf = True
        while verf:
            op = int(input())

            if op not in (1,2):
                print("Ingresa una opcion válida")
            
            else:
                verf = False

        match op:
            case 1:
                juego()

            case 2:
                return 0

    def juego():
        numeroSecreto = 50 #randint(1, 100)
        intentos = 10

        while intentos > 0:
            print(f"Tienes {intentos} intentos")

            try:
                adivinanza = int(input("Ingresa tu numero: "))

                if adivinanza not in range(1, 100):
                    print("El numero no está dentro de 1 y 100")
                    time.sleep(1)
                    continue

                if adivinanza == numeroSecreto:
                    print("¡Felicidades, adivinaste el numero!")
                    miniMenu(1)

                    return 0

                if adivinanza > numeroSecreto:
                    if adivinanza - numeroSecreto >= 20:
                        print("¡Demasiado alto!")
                    elif 10 <= adivinanza - numeroSecreto <= 19:
                        print("¡Muy alto!")                    
                    else:
                        print("¡Alto. Estás muy cerca!")
                if adivinanza < numeroSecreto:
                    if numeroSecreto - adivinanza >= 20:
                        print("¡Demasiado bajo!")
                    elif 10 <= numeroSecreto - adivinanza <= 19:
                        print("¡Muy bajo!")
                    else:
                        print("¡Bajo. Estás muy cerca!")
            except ValueError:
                print("El numero que ingresaste no es parte del numero que tenes que adivinar")
                time.sleep(1)
                print("Por favor, ingresa un numero del 1 al 100")
                time.sleep(1)

            intentos -= 1


        print("¡Te quedaste sin intentos!")
        time.sleep(2)
        print("¡No te preocupes, puedes intentarlo de nuevo!")
        time.sleep(1)
        miniMenu(0)


    explicarReglas()
    time.sleep(2)
    miniMenu(0)

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

# Inicializamos el tablero de juego
tablero = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]

# Variable para llevar el control del ganador
ganador = None

def tateti():
    global ganador
    print("Empieza el juego")
    ver_tablero()

    for i in range(5):
        print("Turno del jugador 1 - X")
        valor = "X"
        # Jugador 1 hace su jugada
        jugada(valor)
        huboganador()
        if ganador == "X":
            print("Felicidades! Jugador 1 Ganador del juego")
            break

        if ganador is None and i < 4:
            print("Turno del jugador 2 - O")
            valor = "O"
            # Jugador 2 hace su jugada
            jugada(valor)
            huboganador()

            if ganador == "O":
                print("Felicidades! Jugador 2 Ganador del juego")
                break

    if ganador is None:
        print("Empataron el juego")

def ver_tablero():
    """ Muestra el tablero de juego """
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("---------")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("---------")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

def huboganador():
    """ Revisa si hay un ganador """
    global ganador
    controlLinea()
    controlVertical()
    controlDiagonal()

def controlLinea():
    """ Verifica si hay una línea ganadora en el tablero """
    global ganador
    if tablero[0] == tablero[1] == tablero[2] != "-":
        ganador = tablero[0]
    elif tablero[3] == tablero[4] == tablero[5] != "-":
        ganador = tablero[3]
    elif tablero[6] == tablero[7] == tablero[8] != "-":
        ganador = tablero[6]

def controlVertical():
    """ Verifica si hay una columna ganadora """
    global ganador
    if tablero[0] == tablero[3] == tablero[6] != "-":
        ganador = tablero[0]
    elif tablero[1] == tablero[4] == tablero[7] != "-":
        ganador = tablero[1]
    elif tablero[2] == tablero[5] == tablero[8] != "-":
        ganador = tablero[2]

def controlDiagonal():
    """ Verifica si hay una diagonal ganadora """
    global ganador
    if tablero[0] == tablero[4] == tablero[8] != "-":
        ganador = tablero[0]
    elif tablero[2] == tablero[4] == tablero[6] != "-":
        ganador = tablero[2]

def jugada(valor):
    """ Realiza la jugada de un jugador """
    anoto = False
    while not anoto:
        try:
            # Pide al jugador que elija una posición
            posicion = int(input(f"Elige una posición del 1 al 9 para {valor}: ")) - 1
            
            if 0 <= posicion < 9 and tablero[posicion] == "-":
                tablero[posicion] = valor
                anoto = True
                ver_tablero()
            else:
                print("Esa posición ya está ocupada o es inválida. Intenta nuevamente.")
        except ValueError:
            print("Por favor ingresa un número válido del 1 al 9.")

def multiplicaciones():
    print("¡¡¡Bienvenido!!! ¡A Multiplicar!")
    #Ciclo repetitivo infinito.
    j = True
    while j:
        #Se definen dos número random como factores y se calcula el producto.
        factor1 = random.randint(1, 10)
        factor2 = random.randint(1, 10)
        producto = factor1*factor2
        #El resultado de la multiplicación se almacena en un vector.
        opciones = [producto]
        #Al vector, se añaden dos números random diferentes al resultado, que serán las opciones para el usuario.
        while (len(opciones) < 3):
            opcion = random.randint(1, 100)
            if opcion != producto:
                opciones.append(opcion)
        #Se mezclan los elementos del vector.
        random.shuffle(opciones)
        #Se muestra en pantalla la operación.
        print(f"Cuál es el resultado de {factor1}x{factor2}?")
        #Se muestran en pantalla las opciones.
        for i in range(0, 3):
            print(f"Opción {i+1}. {opciones[i]}")
        print("Opción 4. Volver al menú principal")
        #Se pide al usuario que elija una opción.
        k = True
        while k: 
            eleccion = int(input("Ingrese su respuesta: "))
            match eleccion:
                #Si el usuario ingresa la opción 1, 2 o 3, se muestra por pantalla si su respuesta fue acertada o equivocada.
                case 1 | 2 | 3:
                    if opciones[eleccion-1] == producto:
                        print("¡Felicidades! Respuesta correcta.")
                        k = False
                        time.sleep(3)
                    else:
                        print(f"Respuesta equivocada. El resultado correcto era {producto}. ¡No te rindas, inténtalo de nuevo!")
                        k = False
                        time.sleep(4)                        
                #Si el usuario ingresa la opción 4, sale del juego actual y regresa al menú principal.
                case 4:
                    j = False
                    k = False                                            
                #Si el usuario ingresa cualquier otro valor fuera del rango de opciones, se mostrará por pantalla el error
                #y se le pedirá ingresar una opción válida.
                case _:
                    print("Error: Debe ingresar una opción válida(1, 2, 3 o 4)")

print("¡¡¡BIENVENIDOS A COROLLA!!!")
z = True
while z:
    print("¿A qué deseas jugar?")
    print(" 1. Multiplicaciones \n 2. Blackjack \n 3. Adivina el número \n 4. Ta Te Ti \n 5. Salir")
    seleccion = int(input("Seleccione una opción: "))
    match seleccion:
        case 1:
            multiplicaciones()
        case 2:
            blackjack()
        case 3:
            AdivinaElNumero()
        case 4:
            tateti()
        case 5:
            z = False
        case _:
            print("Debe ingresar una opción válida")