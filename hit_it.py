from turtle import *

class Sprite(Turtle):
    def __init__(self,col,forma,x,y):
        super().__init__()
        self.penup()
        self.color('black',col)
        self.shape(forma)
        self.goto(x,y)
        self.setheading(90)


player = Sprite(x=0,y=-150,forma='turtle',col='yellow')
enemy1 = Sprite(x=150,y=50,forma='square',col='red')
enemy2 = Sprite(x=-150,y=-50,forma='square',col='red')
goal = Sprite(x=0,y=150,forma='triangle',col='green')



