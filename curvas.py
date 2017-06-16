from turtle import *

speed(0)
def curva():
    for x in range(200):
        rt(1)
        fd(1)

color('red','pink')
pensize(3)
begin_fill()
lt(140)
fd(111.65)
curva()
lt(120)
curva()
fd(111.65)
end_fill()
done()