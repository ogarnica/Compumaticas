ano = int(input('elige el ano: '))
print(ano)
if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print('es bisiesto')
        else:
            print('no es bisiesto')
    else:
        print('es bisiesto')
else:
    print('no es bisiesto')