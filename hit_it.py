from turtle import *

class Sprite(Turtle):
    def __init__(self,x,y,col,forma):
        super().__init__()
        self.penup()
        self.goto(x,y)
        self.color('black',col)
        self.shape(forma)
        self.left(90)

player = Sprite(x=0,y=-150,col='yellow',forma='turtle')
enemy1 = Sprite(x=-150,y=-100,col='red',forma='square')
enemy2 = Sprite(x=150,y=100,col='red',forma='square')
goal = Sprite(x=0,y=150,col='green',forma='triangle')
