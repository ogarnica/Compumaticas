import turtle
import colorsys

def estrella(tamano):
    for x in range(5):
        turtle.fd(tamano)
        turtle.rt(144)

turtle.speed(0)
turtle.pensize(2.5)

for a in range(1, 10000000, 15):
    color = colorsys.hsv_to_rgb(a / 101, 1.0, 1.0)
    turtle.pencolor(color)
    estrella(a)
    turtle.lt(15)
turtle.done()
