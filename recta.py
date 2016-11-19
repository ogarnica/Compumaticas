primer_numero = int(input('primer numero'))
ultimo_numero = int(input('ultimo numero'))
cortes = int(input('cuantos cortes'))

distancia = (ultimo_numero - primer_numero)/(cortes+1)
for x in range(primer_numero, cortes+1):
    am = primer_numero + x * distancia
    print(am)