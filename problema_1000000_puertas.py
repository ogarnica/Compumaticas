puertas = int(input('cuantas puertas quieres: '))
for x in range(puertas+1):
    if x**0.5%1:
        estado = 'c'
    else:
        estado = 'a'
    print(x, estado)