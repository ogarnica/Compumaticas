import time
def final():
    if siono=='si':
        print('BIEN')
    if siono=='no':
        pcorrecta=input('cual seria la palabra al reves: ')
        if pcorrecta==daolavuelta:
            print('(enfadado) Pero si te lo habia dicho! ')
        else:
            print('la palabra que te he dicho es la correcta. Mentiroso, no me engañes')
print('######################################')
time.sleep(0.1)
print('# En este programa tu me introducirás una palabra y yo te la escribir al revés. Por ej. pan=nap #')
time.sleep(0.1)
print('######################################')
time.sleep(0.1)
print('Ahora te toca a ti introducir la palabra')
palabra=input('')
nletras=len(palabra)
print('empezando a deducir...')
time.sleep(1)
print('espera')
time.sleep(0.5)
print('tu palabra no tendrá',nletras,'letras verdad?')
time.sleep(1)
print('pero...')
time.sleep(0.4)
print('como la pongo al revés?')
time.sleep(1)
print('estoy procesando la información')
time.sleep(3)
print('(temblando) ehh')
time.sleep(1)
daolavuelta=palabra[: : -1 ]
if daolavuelta==palabra:
    print('esa palabra me suena a un palindromo')
else:
    print('no será',daolavuelta,', verdad?')
print('si es correcto escribe si')
time.sleep(1)
print('pero... si no lo tengo bien escribe no..')
print('esta bien (si o no)?')
siono=input()
final()

