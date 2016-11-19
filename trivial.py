import random

listas = {'cual es la capital de espana ':'madrid',
'cual es la capital de croacia':'zagreb',
'cual es la capital de inglaterra':'londres',
'como se dice xD en binario':'0111 1000 0100 0100',
'como se escribe 16 en binario':'10000',
'como se escribe 10 en biario':'1010',
'como se escribe hola en chino':'ni hao'}

juego = True
while juego == True:
    score = 0
    numero_preguntas = int(input('cuantas preguntas quieres?: '))
    for x in range(numero_preguntas):
        preguntas = (random.choice(list(listas.keys())))
        respuestas = listas[preguntas]
        print('pregunta '+str(x+1))
        print(preguntas + '?')
        guess = input('>>>')
        if guess.lower() == respuestas.lower():
            print('correcto')
            score += 10
            print('score = ', str(score))
        else:
            print('incorrecto')
    print('score = ', str(score))
    sino = input('quieres seguir si/no: ')
    if sino == 'si':
        juego = True
    else:
        juego = False
