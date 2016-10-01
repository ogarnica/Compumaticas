loop = 1
while loop == 1:
    numero1 = float(input('di un numero     '))
    numero2 = float(input('di otro numero     '))

    if numero1 == 0 and numero2 == 0:
        print('hay soluciones infinitas')
    else:
        if numero1 == 0 and numero2 != 0:
            print('no hay soluciones')
        else:
            if numero1 != 0:
                print(numero2 / numero1)
    continuar = input ( 'quieres continuar     ' )
    if continuar == 'si':
        loop = 1
    else:
        if continuar == 'no':
            loop = 0