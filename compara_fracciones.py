import random as r
numero = int(input('di el numero: '))
lista = []
for x in range(1, numero + 1):
    for y in range(0, numero + 1):
        print(y, '/', x, '=', y/x)
        lista.append(y)
        lista.append(x)
#print(lista)
ele1 = r.randrange(0, numero * (numero+1), 2)
ele2 = r.randrange(0, numero * (numero+1), 2)
ele1 = lista[ele1-1]
ele12 = lista[ele1]
ele2 = lista[ele2-1]
ele22 = lista[ele2]

print('\n', '\n')
while True:
    if ele1/ele12 == ele2/ele22:
        ele1 = r.randrange(0, numero * (numero + 1), 2)
        ele2 = r.randrange(0, numero * (numero + 1), 2)
        ele1 = lista[ele1]
        ele12 = lista[ele1 + 1]
        ele2 = lista[ele2]
        ele22 = lista[ele2 + 1]
    else:
        break

if ele1/ele12 > ele2/ele22:
    print(ele1, '/', ele12, 'es mayor a', ele2, '/', ele22)

if ele1/ele12 < ele2/ele22:
    print(ele1, '/', ele12, 'es menor a', ele2, '/', ele22)