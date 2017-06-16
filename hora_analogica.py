import datetime
import time
import turtle as t

t.hideturtle()
t.pensize(2)
t.speed(0)

def reloj():
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color('black')
    t.circle(100)
    t.penup()
    t.pendown()

def poner_hora():
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.right(hour*360/12)
    t.color('green')
    t.pendown()
    t.forward(50)

def poner_min():

    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.right(6 * mi)
    t.color('blue')
    t.pendown()
    t.forward(90)

def poner_sec():
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.right(6 * sec)
    t.color('red')
    t.pendown()
    t.forward(90)

for x in range(10):
    hour = datetime.datetime.now().hour
    mi = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    t.setheading(360)
    t.clear()
    reloj()
    poner_hora()
    poner_min()
    poner_sec()
    t.penup()
    t.goto(0, -100)
    t.pendown()
    time.sleep(1)
