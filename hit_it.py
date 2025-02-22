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

class Enemy(Sprite):
    def set_move(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x 
        self.start_y = start_y 
        self.end_x = end_x 
        self.end_y = end_y 
        self.goto(start_x, start_y)
        self.setheading(self.towards(end_x, end_y))

    def make_step(self):
        self.forward(50)
        if self.distance(self.end_x, self.end_y) < 50:
            self.set_move(self.end_x, self.end_y, self.start_x, self.start_y )
            

# СОЗДАНИЕ И НАСТРОЙКА ОБЬЕКТОВ
player = Player(x=0, y=-100, figure='circle', col='yellow')
enemy1 = Enemy(x=-100, y=50, figure='square', col='red')
enemy2 = Enemy(x=100, y=-50, figure='square', col='red')
goal = Sprite(x=0, y=100, figure='triangle', col='green')
screen = player.getscreen()
screen.listen()
# ПОДПИСКИ НА СОБЫТИЯ КЛАВИАТУРЫ
screen.onkey(player.move_up,'Up')
screen.onkey(player.move_right,'Right')
screen.onkey(player.move_down,'Down')
screen.onkey(player.move_left,'Left')


enemy1.set_move(-100, 50, 100, 50)
enemy2.set_move(100,-50, -100, -50)

while True:
    enemy1.make_step()
    enemy2.make_step()
    if player.check_collide(goal):
        enemy1.hideturtle()
        enemy2.hideturtle()
        break
    if player.check_collide(enemy1) or player.check_collide(enemy2):
        goal.hideturtle()
        break
