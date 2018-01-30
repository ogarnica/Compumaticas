import random

print(u'\u00A9')

na = []

while True:
    numero_azar = random.randint(111, 999)
    na = str(numero_azar)
    if na[0] == na[1] or na[0] == na[2] or na[1] == na[2]:
        numero_azar = random.randint(111, 999)
    else:
        break

print(numero_azar)

for x in range(1, 11):
    print('Intento #%s' %x)
    eleccion = input()

    def check_todos_mal():
        if eleccion[0] not in na and eleccion[1] not in na and eleccion[2] not in na:
            print('Todos', u'\u274C', 'y en mal pos')


    if na==eleccion:
        print('Bien!  Y gano')

    else:
        for y in range(3):
            if na[y] == eleccion[y]:
                print('Uno', u'\u2713', 'y en pos   ')
            elif na[y] in eleccion:
                print('Uno', u'\u2713', 'pero no en pos   ')
            else:
                if check_todos_mal:
                    check_todos_mal()
                    break

print('Ooooooopsss     Y perdio   Jajajajaja')
exit()