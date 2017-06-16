seguir = 1
while seguir == 1:
    a = 0
    n = int(input('di un numero: '))
    for i in range(1, n+1):
        if n % i == 0:
            a += 1
    if a != 2:
        print('no es primo')
    else:
        print('es primo')
    a = input('quieres seguir s/n: ')
    if a == 's':
        seguir = 1
    else:
        seguir = 0