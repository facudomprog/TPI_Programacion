import random
def ahorcado():
    # Lista de palabras para adivinar
    palabras = ["numeros", "geometria", "lengua", "juego", "escuela"]

    # Elegir una palabra aleatoria de la lista
    palabra = random.choice(palabras)
    letras_adivinadas = []  # Para almacenar las letras adivinadas
    intentos = 6  # Número de intentos permitidos

    # Función para mostrar el progreso del jugador
    def mostrar_palabra():
        palabra_mostrada = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "
        return palabra_mostrada

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra:")
    print(mostrar_palabra())

    # Bucle del juego
    while intentos > 0:
        letra = input("Adivina una letra: ").lower()
            
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Bien! La letra está en la palabra.")
        else:
            intentos -= 1
            print(f"Lo siento, la letra no está en la palabra. Te quedan {intentos} intentos.")
            
        # Mostrar el progreso del jugador
        print(mostrar_palabra())
            
        # Verificar si el jugador ha ganado
        if all(letra in letras_adivinadas for letra in palabra):
            print("¡Felicidades! Has adivinado la palabra.")
            break
    else:
        print("Has perdido. La palabra era:", palabra)
