print('   |   |   ')
print('   |   |   ')
print(' _ | _ | _ ')
print('   |   |   ')
print('   |   |   ')
print(' _ | _ | _ ')
print('   |   |   ')
print('   |   |   ')
print('   |   |   ')
def tablero(T):
    l1 = '  |   |'
    l2 = T[0]+' | '+T[1]+' | '+T[2]
    l3 = '_ | _ | _'
    l4 = l1
    l5 = T[3]+' | '+T[4]+' | '+T[5]
    l6 = l3
    l7 = l1
    l8 = T[6]+' | '+T[7]+' | '+T[8]
    l9 = l1
    print(l1+'\n'+l2+'\n'+l3+'\n'+l4+'\n'+l5+'\n'+l6+'\n'+l7+'\n'+l8+'\n'+l9)
T = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def jugada(T):
    movi = 10
    print('el turno para el primer jugador')
    while movi not in [0,1,2,3,4,5,6,7,8] or T[movi] != ' ':
        movi = int(input('elige'))
        if movi not in [0,1,2,3,4,5,6,7,8]:
            print('otro')
        elif T[movi]!=' ':
            print('ya hay ficha')
    T[movi]='x'
    return T

def vertical(T):
    if T[0]==T[3]==T[6]=='x':
        print('jugador 1 ha ganado')
    elif T[1]==T[4]==T[7]=='x':
        print('jugador 1 ha ganado')
    elif T[2]==T[5]==T[8]=='x':
        print('jugador 1 ha ganado')
    elif T[0]==T[3]==T[6]=='o':
        print('jugador 2 ha ganado')
    elif T[1]==T[4]==T[7]=='o':
        print('jugador 2 ha ganado')
    elif T[2]==T[5]==T[8]=='o':
        print('jugador 2 ha ganado')

def horizontal(T):
    if T[0]==T[1]==T[2]=='x':
        print('jugador 1 a ganado')
    elif T[3]==T[4]==T[5]=='x':
        print('jugador 1 a ganado')
    elif T[6]==T[7]==T[8]=='x':
        print('jugador 1 a ganado')
    elif T[0]==T[1]==T[2]=='o':
        print('jugador 2 a ganado')
    elif T[3]==T[4]==T[5]=='o':
        print('jugador 2 a ganado')
    elif T[6]==T[7]==T[8]=='o':
        print('jugador 2 a ganado')

def diagonal(T):
    if T[0]==T[4]==T[8]=='x':
        print('jugdor 1 ha ganado')
    elif T[2]==T[4]==T[6]=='x':
        print('jugdor 1 ha ganado')
    elif T[0]==T[4]==T[8]=='o':
        print('jugdor 2 ha ganado')
    elif T[2]==T[4]==T[6]=='o':
        print('jugdor 2 ha ganado')

def jugada2(T):
    movi = 10
    print('el turno para el segundo jugador')
    while movi not in [0,1,2,3,4,5,6,7,8] or T[movi] != ' ':
        movi = int(input('elige'))
        if movi not in [0,1,2,3,4,5,6,7,8]:
            print('otro')
        elif T[movi]!=' ':
            print('ya hay ficha')
    T[movi]='o'
    return T

def start(T):
    turno = 1
    diagonal(T) is False
    horizontal(T) is False
    vertical(T) is False
    while diagonal(T) is not True and horizontal(T) is not True and vertical(T) is not True:
        tablero(T)
        if turno == 1:
            T=jugada(T)
            tablero(T)
            diagonal(T)
            horizontal(T)
            vertical(T)
            T=jugada2(T)
            diagonal(T)
            horizontal(T)
            vertical(T)
    if diagonal(T) or horizontal(T) or vertical(T) is not False:
        diagonal(T)
        horizontal(T)
        vertical(T)
start(T)