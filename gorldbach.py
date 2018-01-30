valorMaximo = 10000
rango = range(2,valorMaximo)
primos = list(rango)

for idx in rango:
    esEntero = primos.count(idx)
    if esEntero:
        aBorrar = list(range(idx,valorMaximo,idx))
        tmp = aBorrar.pop(0)
        primos = [x for x in primos if x not in aBorrar]

primos.insert(0,1)
print(primos)
numPrimos = len(primos)
#print "El numero de primos en los primeros %d numeros es: %d" % (valorMaximo, numPrimos)

entrada = int(input('Di un numero par:  '))


def yalotengo(n1, n2):
    print(n1, ' + ', n2)

for a in range(3, entrada):
    if a in primos:
        if entrada - a in primos:
            yalotengo(a, entrada - a)