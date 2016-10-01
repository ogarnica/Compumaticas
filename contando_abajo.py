par_impar = input('par o impar     ')
if par_impar == 'impar':
    for x in range(999, 0, -2):
        print(x)
elif par_impar == 'par':
    for x in range(1000, -1, -2):
        print(x)