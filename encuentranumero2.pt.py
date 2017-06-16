import random
loop = 1
a = int(input('di un numero del 1 al 1000000'))
while loop == 1:
    ordenador = random.randint(1, 1000000)
    if ordenador != a:
        print('este no es',ordenador,'volvere a intentarlo')
    else:
        print(ordenador,'este es tu numero')
        break