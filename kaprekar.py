import sys

nombre_raro = 6174

nume = int(input('num: '))

nu = []
nu.append(5)
nu.append(4)
nu.append(3)
nu.append(2)

def may(lista):
    lista.sort(reverse=True)
    print(lista)


def men(lista):
    lista.sort()
    print(lista)

may(nu)


while True:
    nume = may(nu) - men(nu)
    nu.append(nume[0])
    nu.append(nume[1])
    nu.append(nume[2])
    nu.append(nume[3])
    if nume == nombre_raro:
        print('aki ta')
        sys.exit()
    may(nu)