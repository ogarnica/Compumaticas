import turtle

t = turtle.Pen()
turtle.setup(1000, 800)
t.pensize(3)
t.pencolor('red')

def cuadrado():
    t.begin_fill()
    for x in range(1,4):
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

for y in range(1,5):
    gran_cuadrado()
    t.forward(150)
turtle.done()