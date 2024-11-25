

# Inicializamos el tablero de juego
tablero = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]

# Variable para llevar el control del ganador
ganador = None

def jugar():
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

# Inicia el juego
jugar()
