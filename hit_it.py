from turtle import *

class Sprite(Turtle):
    def __init__(self,x,y,col,forma):
        super().__init__()
        self.penup()
        self.goto(x,y)
        self.color('black',col)
        self.shape(forma)
        self.left(90)

    def move_up(self):
        self.setheading(90)
        self.forward(5)
        
    def move_down(self):
        self.setheading(270)
        self.forward(5)
        
    def move_left(self):
        self.setheading(180)
        self.forward(5)
        
    def move_right(self):
        self.setheading(0)
        self.forward(5)
        
#игровые обьекты
player = Sprite(x=0,y=-150,col='yellow',forma='turtle')
enemy1 = Sprite(x=-150,y=-100,col='red',forma='square')
enemy2 = Sprite(x=150,y=100,col='red',forma='square')
goal = Sprite(x=0,y=150,col='green',forma='triangle')
#обьект экрана
screen = player.getscreen()
screen.listen()
#подписки на события
screen.onkey(player.move_up,'w')
screen.onkey(player.move_down,'s')
screen.onkey(player.move_left,'a')
screen.onkey(player.move_right,'d')
