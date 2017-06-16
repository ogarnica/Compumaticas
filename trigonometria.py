import turtle
import math
t = turtle.Pen()

def punto(i, N, R):
    return R*math.cos(i*2*math.pi/N), R*math.sin(i*2*math.pi/N)
def tabla(k, N, R):
    t.speed(0)
    for i in range(N):
        t.penup()
        x, y = punto(i, N, R)
        t.goto(x, y)
        t.pendown()
        x, y = punto(k*i, N, R)
        t.goto(x, y)
    t.forward(1)
print(punto(800,240,500))
tabla(800, 240, 500)
turtle.done()