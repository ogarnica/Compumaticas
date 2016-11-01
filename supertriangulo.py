import turtle

t = turtle.Pen()
for x in range(1,4):
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