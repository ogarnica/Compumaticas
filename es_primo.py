a = 0
n = int(input('aa'))
for i in range(1, n+1):
    if n % i == 0:
        a += 1
if a != 2:
    print('no es primo')
else:
    print('es primo')
