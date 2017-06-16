import random

print(' __      __    ___        ____  ____  ____  ___        ____  __  __  ____  ____  ____   __    ___  ')
print('(  )    /__\  / __)      (_  _)(  _ \( ___)/ __)      (  _ \(  )(  )( ___)(  _ \(_  _) /__\  / __) ')
print(' )(__  /(__)\ \__ \        )(   )   / )__) \__ \       )___/ )(__)(  )__)  )   /  )(  /(__)\ \__ \ ')
print('(____)(__)(__)(___/       (__) (_)\_)(____)(___/      (__)  (______)(____)(_)\_) (__)(__)(__)(___/ ')

a = random.randint(1, 3)
x = a
if a == 1:
    a = 'cabra'
    b = 'coche'
    c = 'cabra'
elif a == 2:
    a = 'coche'
    b = 'cabra'
    c = 'cabra'
elif a == 3:
    a = 'cabra'
    b = 'cabra'
    c = 'coche'

print('     A       B       C')
def numero1():
    eleccion = input('Elige una puerta(A, B, C): ')
    if x == 1 and eleccion == 'A':
        print('     A       B')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la B')
            print('la B es', b)
        else:
            print('la A es', a)
    if x == 1 and eleccion == 'B':
        print('     A       B')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la A')
            print('la A es', a)
        else:
            print('la B es', b)
    if x == 1 and eleccion == 'C':
        print('     B       C')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la B')
            print('la B es', b)
        else:
            print('la C es', c)
#-----------------------------------------------
def numero2():
    if x == 2 and eleccion == 'A':
        print('     A       B')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la B')
            print('la B es', b)
        else:
            print('la A es', a)
    if x == 2 and eleccion == 'B':
        print('     A       B')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la A')
            print('la A es', a)
        else:
            print('la B es', b)
    if x == 2 and eleccion == 'C':
        print('     A       C')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la A')
            print('la A es', a)
        else:
            print('la C es', c)
#-----------------------------------------------
def numero3():
    if x == 3 and eleccion == 'A':
        print('     A       C')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la C')
            print('la C es', c)
        else:
            print('la A es', a)
    if x == 3 and eleccion == 'B':
        print('     B       C')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la C')
            print('la C es', c)
        else:
            print('la B es', b)
    if x == 3 and eleccion == 'C':
        print('     B       C')
        cambiando = input('quieres cambiar?')
        if cambiando == 'si':
            print('has elegido la B')
            print('la B es', b)
        else:
            print('la C es', c)