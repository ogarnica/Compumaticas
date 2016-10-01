import time
loop = 1
while loop==1:
    nombre = input('¿Cómo te llamas?     ')
    print('Hola',nombre,)
    numero1 = float(input('Di un número: '))
    numero2 = float(input('Di otro:      '))
    print(numero1 + numero2)
    parar = input('¿Quieres parar (si/no)? ')
    if parar == 'si':
        time.sleep(1)
        print('Adios...')
        time.sleep(2)
        loop=0
    if parar == 'no':
        loop=1