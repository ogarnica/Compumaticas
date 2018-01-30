import math

f1 = 'movimiento'
f2 = 'naranja'
f3 = 'ciudadano'
frutas = [f1, f2, f3]

for x in frutas:
    for y in frutas:
        for z in frutas:
            if x == y or x == z or y == z:
                pass
            else:
                print(x, y, z)

print('\n___________NANANANANAN___NANANANANA__________________\n')

for x in frutas:
    for y in frutas:
        if x == y:
            pass
        else:
            print(x, y)

print('\n___________NANANANANAN___NANANANANA__________________\n')

for x in frutas:
    print(x)