import random
import time
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
multiplicaciones()