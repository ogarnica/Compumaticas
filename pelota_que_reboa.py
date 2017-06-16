import turtle as t
import random

t.penup()
t.goto(-200, -200)
t.pendown()

for x in range(4):
    t.fd(400)
    t.lt(90)

while True:
    t.fd(random.randint(0, 100))
    t.lt(random.randint(0, 100))