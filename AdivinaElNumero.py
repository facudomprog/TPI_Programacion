from random import randint
from time import sleep

def AdivinaElNumero():
    def explicarReglas():
        print("¡¡¡Bienvenido a Adivina el Numero!!!")
        sleep(1)
        print("Voy a elegir un numero entre 1 y 100")
        sleep(1)
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
                    sleep(1)
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
                sleep(1)
                print("Por favor, ingresa un numero del 1 al 100")
                sleep(1)

            intentos -= 1


        print("¡Te quedaste sin intentos!")
        sleep(2)
        print("¡No te preocupes, puedes intentarlo de nuevo!")
        sleep(1)
        miniMenu(0)


    explicarReglas()
    sleep(2)
    miniMenu(0)