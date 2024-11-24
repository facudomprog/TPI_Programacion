print("¡¡¡BIENVENIDOS A COROLLA!!!")
z = True
while z:
    print("¿A qué deseas jugar?")
    print(" 1. Multiplicaciones \n 2. Blackjack \n 3. Salir")
    seleccion = int(input("Seleccione un juego: "))
    match seleccion:
        case 1:
            multiplicaciones()
        case 2:
            blackjack()
        case 3:
            z = False
        case _:
            print("Debe ingresar una opción válida")