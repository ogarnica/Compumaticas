import turtle
t = turtle.Pen()
q = turtle.Pen()
t.left(90)
q.left(90)
a = 200
e = 200
def forleft(forward):
    t.left(45)
    t.forward(forward)
def forright(forw):
    q.right(45)
    q.forward(forw)
t.fd(200)
q.forward(200)
for x in range(10):
    a /= 1.5
    forleft(a)
for y in range(10):
    e /= 1.5
    forright(e)
turtle.done()