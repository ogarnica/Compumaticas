import turtle

t = turtle.Pen()
turtle.setup(1250, 800)
t.pencolor('red')
turtle.bgcolor('purple')
t.speed(0.5)
t.pensize(3)
t.shape('square')
x = 1
while True:
    try:
        t.stamp()
        t.forward(x)
        t.left(20)
        x += 0.5
    except KeyboardInterrupt:
        exit()