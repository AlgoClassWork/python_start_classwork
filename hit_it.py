from turtle import *

class Sprite(Turtle):
    def __init__(self, x, y, figure, col):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape(figure)
        self.color('black', col)

class Player(Sprite):
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 5)
    def move_right(self):
        self.goto(self.xcor() + 5, self.ycor())
    def move_down(self):
        self.goto(self.xcor(), self.ycor() -5)
    def move_left(self):
        self.goto(self.xcor() - 5, self.ycor())
    def check_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 20:
            return True
        else:
            return False
            

# СОЗДАНИЕ И НАСТРОЙКА ОБЬЕКТОВ
player = Player(x=0, y=-100, figure='circle', col='yellow')
enemy1 = Sprite(x=-100, y=50, figure='square', col='red')
enemy2 = Sprite(x=100, y=-50, figure='square', col='red')
goal = Sprite(x=0, y=100, figure='triangle', col='green')
screen = player.getscreen()
screen.listen()
# ПОДПИСКИ НА СОБЫТИЯ КЛАВИАТУРЫ
screen.onkey(player.move_up,'Up')
screen.onkey(player.move_right,'Right')
screen.onkey(player.move_down,'Down')
screen.onkey(player.move_left,'Left')

while True:
    if player.check_collide(goal):
        enemy1.hideturtle()
        enemy2.hideturtle()
        break
    if player.check_collide(enemy1) or player.check_collide(enemy2):
        goal.hideturtle()
        break
