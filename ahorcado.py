guesses = ''
palabra = str(input('Di la palabra: '))
vidas = 15
while vidas > 0:

    fail = 0
    for caracter in palabra:
        if caracter in guesses:
            print(caracter)
        else:
            print('_')
            fail += 1
    if fail == 0:
        print('¡Has ganado!')
        break
    guess = input('Di la letra: ')
    guesses += guess
    if guess not in palabra:
        vidas -= 1
        print('Error. Te quedan %s vidas' % vidas)
        if vidas == 0:
            print('GAME OVER   xDxDxD...')