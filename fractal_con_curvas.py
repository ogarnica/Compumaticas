from turtle import *

setheading(90)
def corazon():
    speed(0)
    def curva():
        for x in range(200):
            rt(1)
            fd(1)

    color('red','blue')
    pensize(3)
    begin_fill()
    lt(50)
    fd(111.65)
    curva()
    lt(120)
    curva()
    fd(111.65)
    end_fill()

corazon()
setheading(90)
rt(100)
corazon()
setheading(0)
rt(100)
corazon()
setheading(270)
rt(100)
corazon()
setheading(180)
rt(100)
done()