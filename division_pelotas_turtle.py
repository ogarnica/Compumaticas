import turtle as t

def pintar(bolas):
    t.lt(90)
    for y in range(bolas):
        t.circle(10)
        t.penup()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.pendown()
    t.penup()
    t.lt(90)
    t.fd(bolas*20)
    t.lt(90)
    t.fd(30)
    t.rt(270)
    t.pendown()

dividendo = int(input('dividendo: '))
divisor = int(input('divisor: '))
cociente = dividendo // divisor
resto = dividendo % divisor
for a in range(divisor):
    pintar(cociente)

t.penup()
t.rt(90)
t.fd(50)
t.lt(90)
t.pendown()

pintar(resto)
t.done