alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
texto = 'HELLOWORLD'
caracter = ''
desplazamiento = 2
x = 0
for caracter in texto:
    c = alfabeto.find(texto[x])
    c += desplazamiento
    salida = alfabeto[c]
    print(salida, end='')
    x += 1