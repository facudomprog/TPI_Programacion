import AdivinaElNumero
import multiplicaciones
import Blackjack
import tateti2
while True:
    op = int(input())

    match op:
        case 1:
            AdivinaElNumero.AdivinaElNumero()
        case 2:
            multiplicaciones.multiplicaciones()
        case 3:
            Blackjack.blackjack()
        case 4:
            tateti2.jugar()
        case 5:
            break