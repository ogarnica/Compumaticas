import turtle

t = turtle.Pen()


a = 10
for x in range(20):
    turtle.speed(0)
    t.forward(a)
    t.backward(a)
    t.left(5)
    a += 3
for x in range(7):
    turtle.speed(0)
    t.forward(a)
    t.backward(a)
    t.left(5)
    a -= 1
for x in range(20):
    turtle.speed(0)
    t.forward(a)
    t.backward(a)
    t.left(5)
    a -= 2
turtle.done()