import pygame as pg
import sys
from turtle import *
import random as r

posix = r.randint(-249, 249)
posiy = r.randint(-249, 249)

screen = pg.display.set_mode((250, 250))
penup()
shape("turtle")
t = Pen()
t.speed(0)
sensibility = 25
screen = Screen()

screen.addshape('turtle.png')
t.shape('turtle.png')

running = True


def checkDead():
	if xcor() >= 250 or xcor() <= -250 or ycor() >= 250 or ycor() <= -250:
		print("Dead")
		sys.exit()

def uP():
	seth(90)
	while True:
		fd(1)
		keys = pg.key.get_pressed()
		if keys[pg.K_UP] or keys[pg.K_DOWN] or keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
			break
		if checkDead(): 
				pass

def dowN():
	seth(-90)
	while True:
		fd(1)
		keys = pg.key.get_pressed()
		if keys[pg.K_UP] or keys[pg.K_DOWN] or keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
			break
		if checkDead(): 
				pass
def righT():
	seth(0)
	while True:
		fd(1)
		keys = pg.key.get_pressed()
		if keys[pg.K_UP] or keys[pg.K_DOWN] or keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
			break
		if checkDead(): 
				pass

def lefT():
	seth(180)
	fd(1)
	while True:
		fd(1)
		keys = pg.key.get_pressed()
		if keys[pg.K_UP] or keys[pg.K_DOWN] or keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
			break
		if checkDead(): 
				pass

def apple(posx, posy):
    t.hideturtle()
    t.penup()
    t.goto(posx, posy)
    t.pendown()
    t.showturtle()

def createCircle():
	x = r.randrange(0,250)
	y = r.randrange(0,250)
	penup()
	gotoxy(x,y)
	circle(15)

def drawSquare():
    t.penup()
    t.goto(-250, -250)
    t.pendown()
    for i in range(4):
        t.fd(500)
        t.lt(90)

drawSquare()

apple(posix, posiy)
while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

		keys = pg.key.get_pressed()


		if keys[pg.K_UP]:
			uP()
		if keys[pg.K_DOWN]:
			dowN()
		if keys[pg.K_RIGHT]:
			righT()
		if keys[pg.K_LEFT]:
			lefT()


		if xcor() <= posix + sensibility and xcor() >= posix - sensibility and ycor() <= posiy + sensibility and ycor() >= posiy - sensibility:
			posix = r.randint(-249, 249)
			posiy = r.randint(-249, 249)
			apple(posix, posiy)