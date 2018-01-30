from random import randint
import turtle as t

circles = 20
size = 20
t.speed(0)
t.colormode(255)
def move(length, angle):
    t.right(angle)
    t.forward(length)

def hex():
    t.pendown()
    a = randint(0, 255), randint(0, 255), randint(0, 255)
    t.color(a)
    t.begin_fill()
    for i in range(7):
        move(size,-60)
    t.end_fill()
    t.color(1, 1, 1)
    t.lt(120)
    t.fd(size)
    t.rt(60)
    t.fd(size)
    t.bk(size)
    t.lt(120)
    t.fd(size)
    t.lt(120)
    t.color(a)
    t.fd(size)
    t.end_fill()
    t.penup()


t.penup()
for circle in range(circles):
    if circle == 0:
        hex()
        move(size,-60)
        move(size, -60)
        move(size, -60)
        move(0, 180)
    for i in range(6):
        move(0, 60)
        for j in range(circle+1):
            hex()
            ########################################################
            move(size, -60)
            move(size, 60)
        move(-size, 0)
    move(-size, 60)
    move(size, -120)
    move(0, 60)
