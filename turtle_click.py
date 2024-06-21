from turtle import *
from random import randint
from time import sleep

oleg = Turtle()
oleg.shape('turtle')
oleg.color('black','blue')
oleg.speed(10)
oleg.penup()
oleg.point = 0

def rand_move():
    oleg.goto(randint(-200,200),randint(-200,200))

def catch(x,y):
    oleg.write('Поймали!',font=('Arial',10,'bold'))
    rand_move()
    oleg.point += 1

oleg.onclick(catch)

while oleg.point < 3:
    rand_move()
    sleep(1)

oleg.goto(-150,-20)
oleg.clear()
oleg.write('Ты победил меня человек!',font=('Arial',20,'bold'))
oleg.hideturtle()
