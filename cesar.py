def abcde(txt, d):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    lab = len(abc)
    dcc = {abc(i): abc[(i+d) % lab]for i in range(lab)}
    out = ''
    for c in txt:
        if c in abc:
            new = dcc[c]
        else:
            new = c
        out += new
    return out
while True:
    tex = input('Introduce el texto q quiras saber en CESAR:')
    des = int(input('Introduce el desplazamiento:'))
    siono = input('¿Quieres seguir jugando?S/N:')
    if siono == 'S':
        continue
    else:
        break
