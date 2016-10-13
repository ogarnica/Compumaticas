import random
numero_al_azar = random.randint(1000, 9999)
print('adivina una contraseña de 4 digitos')
for x in range(1, 16):
    numero = int(input())
    if numero == numero_al_azar:
        print('la has adivinado a la %sª' % x)
        exit()
    elif numero < numero_al_azar:
        print('prueba mas alto. Llevas %s intentos' % x)
    elif numero > numero_al_azar:
        print('prueba mas bajo. Llevas %s intentos' % x)

print('Lo has intentado mas de 15 veces.')