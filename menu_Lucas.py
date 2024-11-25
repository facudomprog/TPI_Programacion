import sopaDeLetras
import multiplicaciones
import Blackjack

while True:
    op = int(input())

    match op:
        case 1:
            sopaDeLetras.funcionar()
        case 2:
            multiplicaciones.multiplicaciones()
        case 3:
            Blackjack.blackjack()
