a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
t1 = int(input('t1: '))
t2 = int(input('t2: '))

if a*c == c*b:
    print('No tiene soluciones idiota!!!!!!!!')
    exit()

res = 1/(a*d-c*b)


alfa = d*res
beta = -c*res
gamba = -b*res
delta = a*res

print(alfa, '|', beta)
print('---------------')
print(gamba, '|', delta)
