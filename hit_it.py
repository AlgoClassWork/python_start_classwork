from turtle import *
# Описываем наших персонажей
class Sprite(Turtle):
    def __init__(self,col,forma,x,y):
        super().__init__()
        self.penup()
        self.color('black',col)
        self.shape(forma)
        self.goto(x,y)
        self.setheading(90)

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


# Создаем наших игровых персонажей
player = Sprite(x=0,y=-150,forma='turtle',col='yellow')
enemy1 = Sprite(x=150,y=50,forma='square',col='red')
enemy2 = Sprite(x=-150,y=-50,forma='square',col='red')
goal = Sprite(x=0,y=150,forma='triangle',col='green')
# Создаем обьект экрана
screen = player.getscreen()
screen.listen()
# Подписки на события клавиатуры
screen.onkey(player.move_up,'Up')
screen.onkey(player.move_down,'Down')
screen.onkey(player.move_left,'Left')
screen.onkey(player.move_right,'Right')







