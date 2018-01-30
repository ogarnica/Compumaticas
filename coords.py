def write():
    file = open('coordenadas.txt','a',encoding='utf-8')

    codx = int(input('Coordenada x: '))
    cody = int(input('Coordenada y: '))

    cods = ('%i, %i\n' %(codx, cody))
    file.write(cods)

write()