numero = input('num: ')
numero = list(numero)
long = len(numero)
binary = 0
for x in range(long):
    binary += int(numero[x])*(2**(long-x-1))
print(binary)