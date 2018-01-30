numero = str(1234)
dicho = input('a')
b = []
c = []

for x in range(4):
    if dicho[x] == numero[x]:
        b.append(dicho[x])
print(len(b),' bull')
for y in range(4):
    if dicho[y] in numero and dicho[y] not in b:
        c.append(dicho[y])
print(len(c),' cow')