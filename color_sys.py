import turtle as t
import colorsys
t.speed(0)
t.pensize(1.5)
a = 0
for x in range(500):
    color = colorsys.hsv_to_rgb(x/101, 1.0, 1.0)
    t.pencolor(color)
    t.fd(20+a)
    t.lt(120)
    t.fd(20+a)
    t.lt(120)
    t.fd(20+a)
    t.lt(5)
    a += 0.7