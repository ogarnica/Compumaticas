import random

veces = int(input('¿cuantas veces?: '))
score_ord = 0
score_pers = 0

for x in range(veces):
    yo = int(input('elige 1 para piedra, 2 para papel, 3 para tijeras, 4 para lagarto y 5 para spock: '))
    ordenador = random.randint(1, 6)
    if yo == 1 and ordenador == 1:
        print('empate. Los dos habeis sacado piedra')
    if yo == 1 and ordenador == 2:
        print('ordenador gana. Ha sacado papel')
        score_ord += 1
    if yo == 1 and ordenador == 3:
        print('tu ganas. Ordenador ha sacado tijeras')
        score_pers += 1
    if yo == 1 and ordenador == 4:
        print('tu ganas. Ordenador ha sacado lagarto')
        score_pers += 1
    if yo == 1 and ordenador == 5:
        print('ordenador gana. Ha sacado spock')
        score_ord += 1
    if yo == 2 and ordenador == 1:
        print('tu ganas. Ordenador ha sacado piedra')
        score_pers += 1
    if yo == 2 and ordenador == 2:
        print('empate. Los dos habeis sacado papel')
    if yo == 2 and ordenador == 3:
        print('ordenador gana. Ha sacado tijeras')
        score_ord +=1
    if yo == 2 and ordenador == 4:
        print('ordenador gana. Ha sacado lagarto')
        score_ord += 1
    if yo == 2 and ordenador == 5:
        print('tu ganas. Ordenador ha sacado spock')
        score_pers += 1
    if yo == 3 and ordenador == 1:
        print('ordenador gana. Ha sacado piedra')
        score_ord += 1
    if yo == 3 and ordenador == 2:
        print('tu ganas. Ordenador ha sacado papel')
        score_pers  += 1
    if yo == 3 and ordenador == 3:
        print('empate. Los dos habeis sacado tijeras')
    if yo == 3 and ordenador == 4:
        print('tu ganas. Ordenador ha sacado lagarto')
        score_pers += 1
    if yo == 3 and ordenador == 5:
        print('ordenador gana. Ha sacado spock')
        score_ord += 1
    if yo == 4 and ordenador == 1:
        print('ordenador gana. Ha sacado piedra')
        score_ord += 1
    if yo == 4 and ordenador == 2:
        print('tu ganas. Ordenador ha sacado papel')
        score_pers += 1
    if yo == 4 and ordenador == 3:
        print('ordenador gana. Ha sacado tijeras')
        score_ord += 1
    if yo == 4 and ordenador == 4:
        print('empate. Los dos habeis sacado lagarto')
    if yo == 4 and ordenador == 5:
        print('tu ganas. Ordenador ha sacado spock')
        score_pers += 1
    if yo == 5 and ordenador == 1:
        print('tu ganas. Ordenador ha sacado piedra')
        score_pers += 1
    if yo == 5 and ordenador == 2:
        print('ordenador gana. Ha sacado papel')
        score_ord += 1
    if yo == 5 and ordenador == 3:
        print('tu ganas. Ordenador ha sacado tijeras')
        score_pers += 1
    if yo == 5 and ordenador == 4:
        print('ordenador gana. Ha sacado lagarto')
        score_ord += 1
    if yo == 5 and ordenador == 5:
        print('empate. Los dos habeis sacado spock')

if score_ord < score_pers:
    print('Tu has ganado', score_pers,' ',score_ord)
elif score_ord > score_pers:
    print('Ordenador gana', score_ord,' ',score_pers)