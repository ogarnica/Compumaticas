import random

# Definicion de variables ----------------------------
score_ord = 0
score_per = 0

empate_msg = 'Empate. Los dos habeis sacado'
per_msg = 'Tu ganas. Ordenador ha sacado'
ord_msg = 'Ordenador gana. Ha sacado'
opciones = ['piedra', 'tijera', 'lagarto', 'papel', 'spock']
ganar = {"piedra": ['tijera', 'lagarto'],
         "papel": ['piedra', 'spock'],
         "tijera": ['papel', 'lagarto'],
         "lagarto": ['papel', 'spock'],
         "spock": ['tijera', 'piedra']}
# ----------------------------------------------------

num_partidas = int(input('¿Cuantas partidas quieres jugar?: '))

for x in range(num_partidas):
    jugada_per = input('Elige piedra, papel, tijeras, lagarto o spock: ')
    jugada_ord = random.choice(opciones)
    if jugada_ord == jugada_per:
        print(empate_msg, jugada_ord)
    elif jugada_ord in ganar[jugada_per]:
        print(per_msg, jugada_ord)
        score_per += 1
    else:
        print(ord_msg, jugada_ord)
        score_ord += 1

if score_ord < score_per:
    print('Tu has ganado', score_per, 'veces y el ordenador', score_ord, 'veces.')
else:
    print('Ordenador ha ganado', score_ord, 'veces y tu has ganado', score_per, 'veces.')
