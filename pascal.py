def pascal_triangulo(lista):
    resultado = [1]
    for i in range(len(lista)-1):
        resultado.append(lista[i]+lista[i+1])
    resultado.append(1)
    return resultado

def triangulo(triangulo):
    tr = [1]
    tri = []
    tri.append(pascal_triangulo(tri))
    for x in range(triangulo-1):
        tri = pascal_triangulo(tri)
        print(tri)
print('[1]')
