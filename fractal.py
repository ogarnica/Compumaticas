import turtle
turtle.speed(0)
turtle.penup()
turtle.goto(-500, 0)
turtle.pendown()
def triangulo(tamano):
    turtle.fd(25)
    turtle.lt(45)
    turtle.fd(tamano)
    turtle.rt(90)
    turtle.fd(tamano)
    turtle.lt(45)
    turtle.fd(25)
def grande():
    triangulo(25)
    turtle.lt(45)
    triangulo(25)
    turtle.rt(90)
    triangulo(25)
    turtle.lt(45)
    triangulo(25)
def gigante():
    grande()
    turtle.lt(45)
    grande()
    turtle.rt(90)
    grande()
    turtle.lt(45)
    grande()
gigante()
turtle.rt(90)
gigante()
turtle.rt(90)
gigante()
turtle.rt(90)
gigante()
turtle.done()
