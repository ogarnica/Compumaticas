numero = int(input('di el numero para hacer el factorial: '))
resultado = 1
if numero > 0:
    for numero in range(numero, 1, -1):
        resultado = resultado * numero
    print(resultado)
if numero == 0:
    print('1')
if numero < 0:
    for numero in range(numero, -1, 1):
        resultado = resultado * numero
    print(-resultado)