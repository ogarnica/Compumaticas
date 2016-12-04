numero = int(input('di el numero'))
unidad = input('escribe la unidad')

if unidad == 'mm':
    print('cm = ', numero/10)
    print('dm = ', numero/100)
    print('m = ', numero/1000)
elif unidad == 'cm':
    print('mm = ', numero/0.1)
    print('dm = ', numero/10)
    print('m = ', numero/100)
elif unidad == 'dm':
    print('mm = ', numero/0.01)
    print('cm = ', numero/0.1)
    print('m = ', numero/10)
elif unidad == 'm':
    print('mm = ', numero/0.001)
    print('cm = ', numero/0.01)
    print('dm = ', numero/0.1)
