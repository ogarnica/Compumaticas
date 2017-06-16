def farey():
    numero = int(input('di el numero: '))
    for x in range(1, numero+1):
        for y in range(1, numero+1):
            print(x,'/',y)