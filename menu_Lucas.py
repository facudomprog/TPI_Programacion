import sopaDeLetras
import ejemplo
import vlackyack

while True:
    op = int(input())

    match op:
        case 1:
            sopaDeLetras.funcionar()
        case 2:
            ejemplo.multiplicaciones()
        case 3:
            vlackyack.blackjack()
