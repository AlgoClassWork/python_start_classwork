from turtle import *

class Sprite(Turtle):
   def __init__(self, x, y, shape, color):
       Turtle.__init__(self)
       self.penup()
       self.goto(x, y)
       self.color(color)
       self.shape(shape)

hero = Sprite(0,-150,'circle','black')
enemy1 = Sprite(-150,-50,'square','red')
enemy2 = Sprite(150,50,'square','red')
goal = Sprite(0,159,'triangle','green')
