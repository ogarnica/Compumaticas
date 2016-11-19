import random

yo = int(input('elige 1 para piedra, 2 para papel, 3 para tijeras, 4 para lagarto y 5 para spock'))

veces = input('cuantas veces')
for x in range(veces):
    ordenador = random.randint(1, 6)
    if yo == 1 and ordenador == 1:
        print('empate. Los dos habeis sacado piedra')
    if yo == 1 and ordenador == 2:
        print('ordenador gana. Ha sacado papel')
    if yo == 1 and ordenador == 3:
        print('tu ganas. Ordenador ha sacado tijeras')
    if yo == 1 and ordenador == 4:
        print('tu ganas. Ordenador ha sacado lagarto')
    if yo == 1 and ordenador == 5:
        print('ordenador gana. Ha sacado spock')
    if yo == 2 and ordenador == 1:
        print('tu ganas. Ordenador ha sacado piedra')
    if yo == 2 and ordenador == 2:
        print('empate. Los dos habeis sacado papel')
    if yo == 2 and ordenador == 3:
        print('ordenador gana. Ha sacado tijeras')
    if yo == 2 and ordenador == 4:
        print('ordenador gana. Ha sacado lagarto')
    if yo == 2 and ordenador == 5:
        print('tu ganas. Ordenador ha sacado spock')
    if yo == 3 and ordenador == 1:
        print('ordenador gana. Ha sacado piedra')
    if yo == 3 and ordenador == 2:
        print('tu ganas. Ordenador ha sacado papel')
    if yo == 3 and ordenador == 3:
        print('empate. Los dos habeis sacado tijeras')
    if yo == 3 and ordenador == 4:
        print('tu ganas. Ordenador ha sacado lagarto')
    if yo == 3 and ordenador == 5:
        print('ordenador gana. Ha sacado spock')
    if yo == 4 and ordenador == 1:
        print('ordenador gana. Ha sacado piedra')
    if yo == 4 and ordenador == 2:
        print('tu ganas. Ordenador ha sacado papel')
    if yo == 4 and ordenador == 3:
        print('ordenador gana. Ha sacado tijeras')
    if yo == 4 and ordenador == 4:
        print('empate. Los dos habeis sacado lagarto')
    if yo == 4 and ordenador == 5:
        print('tu ganas. Ordenador ha sacado spock')
    if yo == 5 and ordenador == 1:
        print('tu ganas. Ordenador ha sacado piedra')
    if yo == 5 and ordenador == 2:
        print('ordenador gana. Ha sacado papel')
    if yo == 5 and ordenador == 3:
        print('tu ganas. Ordenador ha sacado tijeras')
    if yo == 5 and ordenador == 4:
        print('ordenador gana. Ha sacado lagarto')
    if yo == 5 and ordenador == 5:
        print('empate. Los dos habeis sacado spock')