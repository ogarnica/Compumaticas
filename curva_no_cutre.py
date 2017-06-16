from turtle import *

def parabola(x,a=0.250,b=-10,c=0):
    return a*x**2+b*x+c

pen = Pen()
pen.color('green')
pen.width(3)
pen.goto(0, 0)
pen.down()
for x in range(0, 51):
    pen.goto(x, parabola(x))
pen.up()
pen.goto(-100, 100)
pen.color('blue')
pen.write('PRO')
done()