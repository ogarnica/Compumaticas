numero = [1, 2, 3, 4]
dicho = input('a')

for x in range(4):
    if dicho[x] == numero[x]:
        print(dicho[x], 'bull')
for y in range(4):
    if dicho[y] in numero:
        print(dicho[y], 'cow')