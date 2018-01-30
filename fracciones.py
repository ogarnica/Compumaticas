numero = int(input('di el numero: '))
for x in range(1, numero + 1):
    for y in range(0, numero + 1):
        print(y, '/', x, '=', y/x)