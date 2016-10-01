import time
print('HOLA')
time.sleep(1)
print('SOY UNA CALCULADORA')
time.sleep(1)
print('Y VOY A HACER OPERACIONES')
time.sleep(1)
loop = 1
while loop == 1:
    numero1 = float(input('di un numero     '))
    numero2 = float(input('di otro     '))
    operacion = input('di la operacion     ')
    if operacion == '+':
        print(numero1 + numero2)
    else:
        if operacion == '-':
            print(numero1 - numero2)
        else:
            if operacion == '*':
                print(numero1 * numero2)
            else:
                if operacion == '/':
                    print(numero1 / numero2)

    continuar = input('quieres continuar     ')
    if continuar == 'si':
        loop = 1
    else:
        if continuar == 'no':
            loop = 0