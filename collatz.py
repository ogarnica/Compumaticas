x = int(input('elige:'))
for a in range(1, 11111111111111111111111111111111111111111):
    if x%2 == 0:
        print(x)
        x = x/2
    elif x%2 != 0:
        print(x)
        x = 3*x+1
    if x == 1:
        print(1.0)
        print('ya esta. he tardado', a+1, 'veces')
        break