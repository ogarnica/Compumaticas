import turtle, colorsys

#colorsys.rgb_to_hsv(0.5, 0.4, 0.5)
t = turtle.Pen()
t.speed(0)
t.pensize(3)
t.pencolor('red')
for x in range(50):
    t.circle(50)
    t.left(10)
t.pencolor('brown')
for x in range(50):
    t.circle(70)
    t.left(10)
t.pencolor('yellow')
for x in range(50):
    t.circle(90)
    t.left(10)
t.pencolor('purple')
for x in range(50):
    t.circle(110)
    t.left(10)
t.pencolor('blue')
for x in range(50):
    t.circle(130)
    t.left(10)
t.pencolor('green')
for x in range(50):
    t.circle(150)
    t.left(10)
t.pencolor('orange')
for x in range(50):
    t.circle(170)
    t.left(10)
t.pencolor('pink')
for x in range(50):
    t.circle(190)
    t.left(10)
t.pencolor('grey')
for x in range(50):
    t.circle(210)
    t.left(10)
t.pencolor('light green')
for x in range(50):
    t.circle(230)
    t.left(10)
turtle.done()