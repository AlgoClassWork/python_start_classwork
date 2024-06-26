from turtle import *
from random import randint
from time import time

gleb = Turtle()
gleb.penup()
gleb.shape('turtle')
gleb.color('black','blue')
gleb.speed(10)
gleb.left(0)

adolf = Turtle()
adolf.penup()
adolf.shape('turtle')
adolf.color('black','white')
adolf.speed(10)
adolf.left(120)

naruto = Turtle()
naruto.penup()
naruto.shape('turtle')
naruto.color('black','orange')
naruto.speed(10)
naruto.left(240)

def finish(t1,t2,t3):
  t1_outside = abs(t1.xcor()) > 200 or abs(t1.ycor()) > 200 
  t2_outside = abs(t2.xcor()) > 200 or abs(t2.ycor()) > 200 
  t3_outside = abs(t3.xcor()) > 200 or abs(t3.ycor()) > 200 
  game_over = t1_outside or t2_outside or t3_outside 
  return game_over

def catch_gleb(x,y):
  gleb.left(180)

def catch_adolf(x,y):
  adolf.left(180)

def catch_naruto(x,y):
  naruto.left(180)

gleb.onclick(catch_gleb)
adolf.onclick(catch_adolf)
naruto.onclick(catch_naruto)

start_time = time() 

while True:
  gleb.forward(5)
  gleb.left( randint(-10,10) )
  adolf.forward(5)
  adolf.left( randint(-10,10) )
  naruto.forward(5)
  naruto.left( randint(-10,10) )
  if finish(gleb,adolf,naruto):
    break

end_time = time()


gleb.goto(-150,-20)
gleb.clear()
gleb.write('Вы продержались! ' + str(int(end_time- start_time)) + 'с'  ,font=('Arial',20,'bold'))
gleb.hideturtle()
