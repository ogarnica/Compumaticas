import turtle
import math

for x in range(1, 101):
    t = x / 10 * math.pi
    x = (1 + 5 * t) * math.cos(t)
    y = (1 + 5 * t) * math.sin(t)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.stamp()
