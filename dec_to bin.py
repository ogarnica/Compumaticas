numero = int(input('num: '))
a = []
while True:
    rest = numero%2
    if numero == 0:
        break
    else:
        a.append(rest)
    numero = numero // 2
print(a)
for x in range(len(a)+1):
    a[x] = a[-x-1]
print(a)