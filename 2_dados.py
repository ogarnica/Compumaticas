import random
import time


print('agitando dados...')
time.sleep(1)
print('jugador 1, estos son tus dados:')
p1d1 = random.randint(1, 6)
print(p1d1)
p1d2 = random.randint(1, 6)
print(p1d2)
time.sleep(1)

print('agitando dados...')
time.sleep(1)
print('jugador 2, estos son tus dados:')
p2d1 = random.randint(1, 6)
print(p2d1)
p2d2 = random.randint(1, 6)
print(p2d2)

suma1 = p1d1 + p1d2
suma2 = p2d1 + p2d2

if p1d1 == p1d2:
    if p2d1 == p2d2:
        if suma1 > suma2:
            print('jugador 1 ha ganado')
            exit()
        elif suma1 < suma2:
            print('jugador 2 ha ganado')
            exit()
        elif suma1 == suma2:
            print('ha sido empate')
            exit()
    else:
        print('jugador 1 ha ganado')
        marcador1 += 1
        exit()

if p2d1 == p2d2:
    if p1d1 == p1d2:
        if suma1 > suma2:
            print('jugador 1 ha ganado')
            marcador1 += 1
            exit()
        elif suma1 < suma2:
            print('jugador 2 ha ganado')
            marcador2 += 1
            exit()
        elif suma1 == suma2:
            print('ha sido empate')
            exit()
    else:
        print('jugador 2 ha ganado')
        exit()

if suma1 > suma2:
    print('jugador 1 ha ganado')
    exit()
elif suma1 < suma2:
    print('jugador 2 ha ganado')
    exit()
elif suma1 == suma2:
    print('ha sido empate')
    exit()


if suma1 > suma2:
    print('jugador 1 ha ganado')
    exit()
elif suma1 < suma2:
    print('jugador 2 ha ganado')
    exit()
elif suma1 == suma2:
    print('ha sido empate')
    exit()
