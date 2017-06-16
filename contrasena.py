import random
ordopers = input('quien elige la contraseña?: ')
if ordopers == 'yo':
    contraseña = (input('contraseña: '))
    if len(contraseña) >= 8:
        print('es segura')
    elif len(contraseña) < 8 and len(contraseña) > 4:
        print('es poco segura')
    elif len(contraseña) <= 4:
        print('no es nada segura')
elif ordopers == 'tu':
    a = random.randint(1, 90000000000000000)
    print(a)