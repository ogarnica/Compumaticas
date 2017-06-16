import time
import random

print('voy a adivinar un numero del 1 al 20')
print('piensa un numero')
time.sleep(3)
print('ya lo has pensado?')
print('empecemos')
time.sleep(1)
n10 = input('es el 10?')
if n10 == 'si':
    print('bien!!!!')
else:
    mom = input('es mayor o menor')
    if mom == 'mayor':
        a = random.randint(11, 20)
    elif mom == 'menor':
        a = random.randint(1, 9)
for x in range(10):
    print('es el', a,'?')
    q = input()
    if q == 'si':
        print('bien!!!!')
        break
    else:
        mom = input('es mayor o menor')
        if mom == 'mayor':
            a = random.randint(a+1, 20)
        elif mom == 'menor':
            a = random.randint(1, a-1)
print('OOOOH')
time.sleep(0.75)
print('HE PERDIDO')