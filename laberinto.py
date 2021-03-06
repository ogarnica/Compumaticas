import turtle as t
import pygame

t.speed(0)
t.title('laberinto')

def cuadradito(tamano, tamano2):
    t.begin_fill()
    t.fd(tamano)
    t.rt(90)
    t.fd(tamano2)
    t.rt(90)
    t.fd(tamano)
    t.rt(90)
    t.fd(tamano2)
    t.end_fill()

def cuadrado():
    t.fd(200)
    t.rt(90)
    t.fd(90)
    t.penup()
    t.fd(20)
    t.pendown()
    t.fd(90)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(90)
    t.penup()
    t.fd(20)
    t.pendown()
    t.fd(90)
    t.goto(0, -90)
    cuadradito(90, 20)
    t.penup()
    t.rt(90)
    t.goto(40, -20)
    t.pendown()
    cuadradito(20, 50)
    t.penup()
    t.rt(90)
    t.goto(110, -20)
    t.pendown()
    cuadradito(20, 90)
    t.penup()
    t.rt(90)
    t.goto(40, -60)
    t.pendown()
    cuadradito(20, 140)
    t.penup()
    t.rt(90)
    t.goto(110, -110)
    t.pendown()
    cuadradito(50, 70)
    t.penup()
    t.rt(90)
    t.goto(0, -200)
    t.pendown()
    cuadradito(90, 90)
    t.penup()
    t.rt(90)
    t.goto(110, -200)
    t.pendown()
    cuadradito(70, 90)
    t.penup()
    t.rt(90)
    t.goto(40, -90)
    t.pendown()
    cuadradito(15, 50)
#    t.penup()
#    t.rt(90)
#    t.goto(180, -80)
#    t.pendown()
#    cuadradito(20, 20)
    t.penup()
    t.rt(90)
    t.goto(90, -75)
    t.pendown()
    cuadradito(15, 20)
    t.penup()
    t.rt(90)
    t.goto(90, -200)
    t.pendown()
    cuadradito(100, 20)
cuadrado()

t.penup()
t.goto(-20, -100)
t.pendown()
t.pencolor('green')
print('esto es un laberinto')
print('muevete con w, s, a, d')
print('empecemos')
pygame.init()
screen = pygame.display.set_mode((500, 350))
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        print('hola')
        t.fd(10)
    if keys[pygame.K_LEFT]:
        print('adios')
        t.fd(-10)

    if keys[pygame.K_UP]:
        print('hola')
        t.rt(30)
    if keys[pygame.K_DOWN]:
        print('adios')
        t.lt(30)