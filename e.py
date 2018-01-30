import math

veces = int(input('veces: '))

e = 1

for x in range(1, veces + 1):
    e += 1/math.factorial(x)

print(e)
print(math.e)
