import turtle as t
t.pensize(5)
t.speed(0)
t.penup()
t.fd(100)
t.lt(90)
t.pendown()
t.circle(100)
t.penup()
t.goto(0, 0)
t.pendown()
for x in range(8):
    t.fd(100)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.lt(45)

t.fd(100)
t.pencolor('red')
t.lt(135)
for e in range(4):
    t.fd(140)
    t.lt(90)
t.pencolor('blue')
t.rt(22.5)
for v in range(8):
    t.fd(75)
    t.lt(45)
t.done()