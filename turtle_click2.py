from turtle import *
from random import randint
from time import time

adolf = Turtle()
oleg = Turtle()
saitama = Turtle()

def start(name,col,angle):
  name.penup()
  name.shape('turtle')
  name.color('black',col)
  name.left(angle)

start(adolf,'black',0)
start(oleg,'blue',120)
start(saitama,'red',240)
