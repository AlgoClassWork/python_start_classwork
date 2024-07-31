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

    def is_collide(self,some_object):
        dist = self.distance(some_object.xcor(),some_object.ycor())
        if dist < 20:
            return True
        else:
            return False
        
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

while True:
    if player.is_collide(goal):
        goal.goto(-150,0)
        goal.write('ТЫ ПОБЕДИЛ',font=('Arial',40,'bold'))
        break
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        enemy1.goto(-150,0)
        enemy1.write('ТЫ ПРОИГРАЛ',font=('Arial',40,'bold'))
        break
player.hideturtle()
enemy1.hideturtle()
enemy2.hideturtle()
goal.hideturtle()
