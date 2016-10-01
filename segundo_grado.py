import math, time
loop = 1
while loop == 1:
    a = int(input('primer numero     '))
    time.sleep(1)
    b = int(input('segundo numero     '))
    time.sleep(1)
    c = int(input('tercer numero     '))
    time.sleep(1)
    d = b**2 - 4 * a * c

    if d == 0:
        x = -b / (2 * a)
        print(x)
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        print(x1)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(x2)
    elif d < 0:
        print('no hay soluciones')

    continuar = input ( 'quieres continuar(si/no)     ' )
    if continuar == 'si':
        loop = 1
    else:
        if continuar == 'no':
            loop = 0