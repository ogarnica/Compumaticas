numero = int(input('escribe un numero de tres cifras: '))
unidades = numero%10
decenas = numero%100-unidades
decenas = int(decenas/10)
centenas = int(numero/100)

suma=unidades+decenas+centenas
print(centenas,' + ',decenas,' + ',unidades,' = ',suma)
