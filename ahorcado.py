print('JUGADOR 1')
palabra = input('DI UNA PALABRA')
print('JUGADOR 2')
print('tiene %s letras' % len(palabra))

for letra in palabra:
    letra = input('di una letra')
    if letra == 'palabra':
        print(letra)
    else:
        print('-')