from turtle import *
from random import randint
from time import time


def finish(name1,name2,name3):
  name1_outside = abs( name1.xcor() ) > 200 or abs( name1.ycor() ) > 200 
  name2_outside = abs( name2.xcor() ) > 200 or abs( name2.ycor() ) > 200 
  name3_outside = abs( name3.xcor() ) > 200 or abs( name3.ycor() ) > 200 
  game_over = name1_outside or name2_outside or name3_outside
  return game_over


def start(name,col,angle):
  name.penup()
  name.shape('turtle')
  name.color('black',col)
  name.left(angle)

def move(name):
  name.forward(5)
  name.left(randint(-10,10))

def catch_adolf(x,y): 
  adolf.left(180)     

def catch_oleg(x,y):  
  oleg.left(180)      

def catch_saitama(x,y): 
  saitama.left(180)     

adolf = Turtle()
oleg = Turtle()
saitama = Turtle()

start(adolf,'black',0)
start(oleg,'blue',120)
start(saitama,'red',240)

adolf.onclick(catch_adolf) 
oleg.onclick(catch_oleg) 
saitama.onclick(catch_saitama) 

while finish(adolf,oleg,saitama) != True:
  move(adolf)
  move(oleg)
  move(saitama)
