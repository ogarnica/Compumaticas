import turtle

t = turtle.Pen()

turtle.title('triangulos')
turtle.bgcolor('blue')
t.pensize(2)
t.pencolor('purple')
lado = float(input('di el lado: '))
escala = float(input('escala: '))
triangulo_2 = escala * lado

t.forward(lado)
t.left(120)
t.forward(lado)
t.left(120)
t.forward(lado)
t.left(120)

t.forward(triangulo_2)
t.left(120)
t.forward(triangulo_2)
t.left(120)
t.forward(triangulo_2)
t.left(120)

turtle.done()
