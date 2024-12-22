from turtle import *

class GameSprite(Turtle):
    def __init__(self, x, y, col, shp):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.color('black', col )
        self.shape(shp)
        self.left(90)

    def move_up(self):
        self.forward(5)

    def move_left(self):
        self.left(10)

    def move_right(self):
        self.right(10)

    def persecution(self, player):
        self.setheading(self.towards(player.xcor(), player.ycor()))
        self.forward(4)

player = GameSprite(x=0, y=-150, col='yellow', shp='turtle')
enemy1 = GameSprite(x=-150, y=-50, col='red', shp='circle')
enemy2 = GameSprite(x=150, y=50, col='red', shp='circle')
goal = GameSprite(x=0, y=150, col='green', shp='triangle')

screen = player.getscreen()
screen.listen()

screen.onkey(player.move_up, 'w')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_right, 'd')

while True:
    enemy1.persecution(player)
    enemy2.persecution(player)
