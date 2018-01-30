import string, re

for nume in range(1, 1001):
    nume_aux = str(nume)
    nume_aux = list(nume_aux)

    long = len(nume_aux)

    rev = []

    for a in range(long-1, -1, -1):
        rev.append(nume_aux[a])

    rev = list(rev)

#    print(rev)
    rev = str(rev)
    nume_aux = str(nume_aux)
    if nume_aux == rev:
        print('El numero '+str(nume)+' es capicua')
#print(len(nume))