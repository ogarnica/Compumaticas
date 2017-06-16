b = 0
veces = int(input('cuantas veces?: '))

for x in range(2, veces+2, 2):
    a = 1/x
    b = b+a
print(b)