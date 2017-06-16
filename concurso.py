import time, random, turtle, math, colorsys
from datetime import datetime


print('         ______    _')
print('|    |  |  __  |  | |          /\ ')
print('|____|  | |  | |  | |         /  \ ')
print('|    |  | |__| |  | |____    /----\ ')
print('|    |  |______|  |______|  /      \ ')

time.sleep(1.5)
print('Esto es un programa con el que puedes jugar a bastantes juegos...')
time.sleep(0.75)
print('Vamos a empezar')
time.sleep(1)

while True:
    print('MENU DE JUEGOS')
    print('1. Piedra papel tijeras lagarto spock')
    print('2. Conversor de medida')
    print('3. Trivial')
    print('4. Leer palabras al reves')
    print('5. Reloj')
    print('6. Ahorcado')
    print('7. DIBUJOS')
    print('8. CODIFICADORES')
    time.sleep(1)
    eleccion = int(input('Elige el numero del juego que quieras: '))
    if eleccion < 1 or eleccion >8:
        print('Elige un numero del 1 al 8')
        time.sleep(2)
    else:
        break

time.sleep(1)
print('Has elegido el',eleccion)
time.sleep(1.25)
if eleccion == 1:

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
        time.sleep(0.75)
        jugada_per = input('Elige piedra, papel, tijeras, lagarto o spock: ')
        time.sleep(0.75)
        jugada_ord = random.choice(opciones)
        if jugada_ord == jugada_per:
            time.sleep(0.75)
            print(empate_msg, jugada_ord)
        elif jugada_ord in ganar[jugada_per]:
            time.sleep(0.75)
            print(per_msg, jugada_ord)
            score_per += 1
        else:
            print(ord_msg, jugada_ord)
            score_ord += 1

    if score_ord < score_per:
        time.sleep(0.75)
        print('Tu has ganado', score_per, 'veces y el ordenador', score_ord, 'veces.')
    else:
        time.sleep(0.75)
        print('Ordenador ha ganado', score_ord, 'veces y tu has ganado', score_per, 'veces.')

if eleccion == 2:
    numero = int(input('di el numero para convertir: '))
    unidad = input('escribe la unidad: ')

    if unidad == 'mm':
        print('cm = ', numero / 10)
        print('dm = ', numero / 100)
        print('m = ', numero / 1000)
    elif unidad == 'cm':
        print('mm = ', numero / 0.1)
        print('dm = ', numero / 10)
        print('m = ', numero / 100)
    elif unidad == 'dm':
        print('mm = ', numero / 0.01)
        print('cm = ', numero / 0.1)
        print('m = ', numero / 10)
    elif unidad == 'm':
        print('mm = ', numero / 0.001)
        print('cm = ', numero / 0.01)
        print('dm = ', numero / 0.1)

if eleccion == 3:
    listas = {'cual es la capital de espana ': 'madrid',
              'cual es la capital de croacia': 'zagreb',
              'cual es la capital de inglaterra': 'londres',
              'como se dice xD en binario': '0111 1000 0100 0100',
              'como se escribe 16 en binario': '10000',
              'como se escribe 10 en biario': '1010',
              'como se escribe hola en chino': 'ni hao'}

    juego = True
    while juego == True:
        score = 0
        numero_preguntas = int(input('cuantas preguntas quieres?: '))
        for x in range(numero_preguntas):
            preguntas = (random.choice(list(listas.keys())))
            respuestas = listas[preguntas]
            print('pregunta ' + str(x + 1))
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

if eleccion == 4:

    def final():
        if siono == 'si':
            print('BIEN')
        if siono == 'no':
            pcorrecta = input('cual seria la palabra al reves: ')
            if pcorrecta == daolavuelta:
                print('(enfadado) Pero si te lo habia dicho! ')
            else:
                print('la palabra que te he dicho es la correcta. Mentiroso, no me engaÃ±es')


    print('######################################')
    time.sleep(0.1)
    print('# En este programa tu me introducirÃ¡s una palabra y yo te la escribir al revÃ©s. Por ej. pan=nap #')
    time.sleep(0.1)
    print('######################################')
    time.sleep(0.1)
    print('Ahora te toca a ti introducir la palabra')
    palabra = input('')
    nletras = len(palabra)
    print('empezando a deducir...')
    time.sleep(1)
    print('espera')
    time.sleep(0.5)
    print('tu palabra no tendrÃ¡', nletras, 'letras verdad?')
    time.sleep(1)
    print('pero...')
    time.sleep(0.4)
    print('como la pongo al revÃ©s?')
    time.sleep(1)
    print('estoy procesando la informaciÃ³n')
    time.sleep(3)
    print('(temblando) ehh')
    time.sleep(1)
    daolavuelta = palabra[:: -1]
    if daolavuelta == palabra:
        print('esa palabra me suena a un palindromo')
    else:
        print('no serÃ¡', daolavuelta, ', verdad?')
    print('si es correcto escribe si')
    time.sleep(1)
    print('pero... si no lo tengo bien escribe no..')
    print('esta bien (si o no)?')
    siono = input()
    final()

if eleccion == 5:

    try:
        while True:
            now = datetime.now()
            dd = str(now.day)
            mm = str(now.month)
            yyyy = str(now.year)
            hour = str(now.hour)
            mi = str(now.minute)
            sec = str(now.second)
            print(dd, '/', mm, '/', yyyy, '  ', hour, ':', mi, ':', sec)
            time.sleep(1)
    except KeyboardInterrupt:
        exit()

if eleccion == 6:
    guesses = ''
    palabra = str(input('Jugador 1, di la palabra: '))
    for l in range(100):
        print(' ')
    vidas = 10
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

if eleccion == 7:
    while True:
        print('MENU DE DIBUJOS')
        print('1. Supercuadrados')
        print('2. Supertriangulos')
        print('3. Fractal de Koch(3Âºgrado)')
        print('4. Espiral')
        print('5. Estrella')
        print('6. Muchos circulos')
        time.sleep(1)
        dibujo = int(input('Elige el dibujo que quieras: '))
        if dibujo < 1 or dibujo > 6:
            print('Elige un numero del 1 al 6')
            time.sleep(2)
        else:
            break
    time.sleep(1)
    print('Has elegido el',dibujo)
    time.sleep(1.25)
    if dibujo == 1:
        t = turtle.Pen()
        turtle.setup(1000, 700)
        t.pensize(3)
        t.pencolor('red')


        def cuadrado():
            t.begin_fill()
            for x in range(1, 4):
                t.left(90)
                t.forward(25)
            t.end_fill()


        def gran_cuadrado():
            t.forward(75)
            cuadrado()
            t.forward(75)
            cuadrado()
            t.forward(75)
            cuadrado()
            t.forward(75)


        for y in range(1, 5):
            gran_cuadrado()
            t.forward(150)
        turtle.done()

    if dibujo == 2:
        t = turtle.Pen()
        for x in range(1, 4):
            t.forward(200)
            t.left(120)


        def triangulo(size):
            t.left(60)
            t.forward(size)
            t.left(120)
            t.forward(size)
            t.left(120)
            t.forward(size)
            t.left(60)


        t.forward(100)
        triangulo(100)
        t.forward(50)
        t.begin_fill()
        triangulo(50)
        t.end_fill()
        t.back(100)
        t.begin_fill()
        triangulo(50)
        t.end_fill()
        t.forward(150)
        t.left(120)
        t.forward(150)
        t.begin_fill()
        triangulo(50)
        t.end_fill()
        turtle.done()

    if dibujo == 3:
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-500, 0)
        turtle.pendown()


        def triangulo(tamano):
            turtle.fd(25)
            turtle.lt(45)
            turtle.fd(tamano)
            turtle.rt(90)
            turtle.fd(tamano)
            turtle.lt(45)
            turtle.fd(25)


        def grande():
            triangulo(25)
            turtle.lt(45)
            triangulo(25)
            turtle.rt(90)
            triangulo(25)
            turtle.lt(45)
            triangulo(25)


        def gigante():
            grande()
            turtle.lt(45)
            grande()
            turtle.rt(90)
            grande()
            turtle.lt(45)
            grande()


        gigante()
        turtle.rt(90)
        gigante()
        turtle.rt(90)
        gigante()
        turtle.rt(90)
        gigante()
        turtle.done()

    if dibujo == 4:

        turtle.pencolor('red')
        turtle.pensize(3)
        turtle.bgcolor('purple')
        for i in range(500):
            a = i / 20 * math.pi
            x = (1 + 5 * a) * math.cos(a)
            y = (1 + 5 * a) * math.sin(a)
            turtle.goto(x, y)
        turtle.done()

    if dibujo == 5:

        def estrella(tamano):
            for x in range(5):
                turtle.fd(tamano)
                turtle.rt(144)


        turtle.speed(0)
        turtle.pensize(2.5)

        for a in range(1, 10000000, 15):
            color = colorsys.hsv_to_rgb(a / 101, 1.0, 1.0)
            turtle.pencolor(color)
            estrella(a)
            turtle.lt(15)
        turtle.done()

    if dibujo == 6:
        t = turtle.Pen()
        t.speed(0)
        t.pensize(3)
        t.pencolor('red')
        for x in range(50):
            t.circle(50)
            t.left(10)
        t.pencolor('brown')
        for x in range(50):
            t.circle(70)
            t.left(10)
        t.pencolor('yellow')
        for x in range(50):
            t.circle(90)
            t.left(10)
        t.pencolor('purple')
        for x in range(50):
            t.circle(110)
            t.left(10)
        t.pencolor('blue')
        for x in range(50):
            t.circle(130)
            t.left(10)
        t.pencolor('green')
        for x in range(50):
            t.circle(150)
            t.left(10)
        t.pencolor('orange')
        for x in range(50):
            t.circle(170)
            t.left(10)
        t.pencolor('pink')
        for x in range(50):
            t.circle(190)
            t.left(10)
        t.pencolor('grey')
        for x in range(50):
            t.circle(210)
            t.left(10)
        t.pencolor('light green')
        for x in range(50):
            t.circle(230)
            t.left(10)
        turtle.done()

if eleccion == 8:
    while True:
        print('MENU DE CODIFICACIOES')
        print('1. Morse')
        print('2. Cesar')
        time.sleep(1)
        codigo = int(input('Elige el numero del juego que quieras: '))
        if codigo < 1 or codigo > 2:
            print('Elige un numero del 1 al 2')
            time.sleep(2)
        else:
            break

    time.sleep(1)
    print('Has elegido el',codigo)
    time.sleep(1.25)
    if codigo == 1:
            codigo = {
                "a": ".-",
                "b": "-...",
                "c": "-.-.",
                "d": "-..",
                "e": ".",
                "f": "..-.",
                "g": "--.",
                "h": "....",
                "i": "..",
                "j": ".---",
                "k": "-.-",
                "l": ".-..",
                "m": "--",
                "n": "-.",
                "o": "---",
                "p": ".--.",
                "q": "--.-",
                "r": ".-.",
                "s": "...",
                "t": "-",
                "u": "..-",
                "v": "...-",
                "w": ".--",
                "x": "-..-",
                "y": "-.--",
                "z": "--..",
                "0": ".....",
                "1": "....-",
                "2": "...--",
                "3": "..---",
                "4": ".----",
                "5": "-----",
                "6": "----.",
                "7": "---..",
                "8": "--...",
                "9": "-....",
                " ": " "}

            while True:
                texto = input('Dime un texto que quieras traducir: ')

                for x in range(len(texto)):
                    print(codigo[texto[x]])

    if codigo == 2:
        def cifra(txt, d):
            abc = 'abcdefghijklmnopqrstuvwxyz'
            lab = len(abc)
            dcc = {abc[i]: abc[(i + d) % lab] for i in range(lab)}
            out = ''
            for c in txt:
                if c in abc:
                    new = dcc[c]
                else:
                    new = c
                out += new
            return out


        while True:
            tex = input('Introduce el texto que quiras saber en CESAR: ')
            des = int(input('Introduce el desplazamiento: '))
            des = int(des)
            print('\nCalculando...')
            print('OK!\n')
            print('ENTRADA:\n' + tex + '\n')
            print('SALIDA:\n' + cifra(tex, des) + '\n')
            siono = input('Â¿Quieres seguir jugando?S/N: ')
            if siono == 'S':
                continue
            else:
                break
