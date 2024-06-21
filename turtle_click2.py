from turtle import *
from random import randint
from time import time

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

adolf.onclick(catch_adolf) #new
oleg.onclick(catch_oleg) #new
saitama.onclick(catch_saitama) #new

while True:
  move(adolf)
  move(oleg)
  move(saitama)
