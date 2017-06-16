import turtle
import math

turtle.pencolor('red')
turtle.pensize(3)
turtle.bgcolor('purple')
for i in range(500):
    a = i/20*math.pi
    x = (1+5*a)*math.cos(a)
    y = (1+5*a)*math.sin(a)
    turtle.goto(x,y)
turtle.done()
