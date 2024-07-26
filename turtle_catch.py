from turtle import *
from random import randint
from time import sleep

naruto = Turtle()
naruto.shape('turtle')
naruto.color('black','orange')
naruto.speed(10)
naruto.penup()
naruto.points = 0 #new

def rand_move():
    naruto.goto(randint(-200,200),randint(-200,200))

def catch(x,y):
    naruto.write('Ай',font=('Arial',15,'bold'))
    naruto.points += 1
    rand_move() #new

naruto.onclick(catch)

while naruto.points < 3: #new
    rand_move()
    sleep(1)

naruto.clear() #new
naruto.goto(-100,0) #new
naruto.write('Ты победил',font=('Arial',30,'bold')) #new
naruto.hideturtle() #new
