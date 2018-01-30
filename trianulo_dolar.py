altura = int(input('elige la altura: '))
alto = altura
altos = altura
altoss = altura
altosss = altura
a = 1
aa = altura-3
dolar = ' $'
euro = ' �'

for x in range(1, 3):
   espacios = alto - 1
   print(espacios*' '+x*dolar)
   alto -= 1

for y in range(3, altura+1):
   spaces = altos - 3
   print(spaces*' '+dolar+a*euro+dolar)
   a += 1
   altos -= 1
b = 1
for q in range(altura, 2, -1):
    print(b*' '+dolar+aa*euro+dolar)
    b += 1
    aa -= 1
w = altura-1
print(w*' '+dolar)


#    $
#   $ $
#  $ € $
# $ € € $
#  $ € $
#   $ $
#    $
