f1 = int(input('factor 1: '))
f2 = int(input('factor 2: '))

suma = 0
a = 1
f1st = []
f2st = []

while True:
    if f1 != 1:
        f1st.append(f1)
        f1 = f1//2
        f2st.append(f2)
        f2 = f2 * 2
        a += 1
    else:
        f1st.append(f1)
        f2st.append(f2)
        break


for x in range(a):
    print(f1st[x], '   ', f2st[x])
    if f1st[x] % 2 != 0:
        suma = suma + f2st[x]

print('Por lo que si eres un poco listo sabras el resultado    Pero tu eres idiotaaaaa   Que es el ', suma)