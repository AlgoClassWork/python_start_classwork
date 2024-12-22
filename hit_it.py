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
        self.left(90)

    def move_right(self):
        self.right(90)

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        self.forward(15)
        if self.distance(self.x_end, self.y_end) < 15:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

player = GameSprite(x=0, y=-150, col='yellow', shp='turtle')
enemy1 = GameSprite(x=-150, y=-50, col='red', shp='circle')
enemy2 = GameSprite(x=150, y=50, col='red', shp='circle')
goal = GameSprite(x=0, y=150, col='green', shp='triangle')

screen = player.getscreen()
screen.listen()

screen.onkey(player.move_up, 'w')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_right, 'd')

enemy1.set_move(-150, -50, 150, -50)
enemy2.set_move(150, 50, -150, 50)

while True:
    enemy1.make_step()
    enemy2.make_step()
