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

def catch_gleb(x,y):
  gleb.left(180)

def catch_adolf(x,y):
  adolf.left(180)

def catch_naruto(x,y):
  naruto.left(180)

gleb.onclick(catch_gleb)
adolf.onclick(catch_adolf)
naruto.onclick(catch_naruto)

while True:
  gleb.forward(5)
  gleb.left( randint(-10,10) )
  adolf.forward(5)
  adolf.left( randint(-10,10) )
  naruto.forward(5)
  naruto.left( randint(-10,10) )

gleb.goto(-150,-20)
gleb.clear()
gleb.write('Красава!',font=('Arial',20,'bold'))
gleb.hideturtle()
