lista1 = input('a: ')
lista2 = input('a: ')
lista1 = list(lista1)
lista2 = list(lista2)
for x in range(len(lista1)+1):
    if lista1[x] in lista2:
        print(lista1[x], 'is in lista1 and lista2')
