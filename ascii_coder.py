a = input('quieres codificar o decodificar')
if a == 'codificar':
    mensaje = input('a: ')
    for x in mensaje:
        print(ord(x), end =' ')

else:
    codigo = input('b: ')
    decodificado = ''
    for y in codigo.split():
        decodificado += chr(int(y))
    print(decodificado, end=' ')