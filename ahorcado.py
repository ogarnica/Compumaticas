guesses = ''
palabra = 'computadora'
vidas = 0
while vidas < 15:

    fail = 0
    for caracter in palabra:
        if caracter in guesses:
            print(caracter)
        else:
            print('_')
            fail += 1
    if fail == 0:
        print('has ganado')
        break
    guess = input('di la letra')
    guesses += guess
    if guess not in palabra:
        vidas -= 1
        print('error')
        if vidas == 0:
            print('GAME OVER   xDxDxD...')