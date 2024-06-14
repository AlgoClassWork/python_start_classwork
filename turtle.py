from turtle import *

class Sprite(Turtle):
    def __init__(self, x, y, shape, color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.shape(shape)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 5)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 5)
    def move_left(self):
        self.goto(self.xcor() - 5, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + 5, self.ycor())


player = Sprite(0,-150,'circle','black')
enemy1 = Sprite(-150,-50,'square','red')
enemy2 = Sprite(150,50,'square','red')
goal = Sprite(0,159,'triangle','green')


scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'w')
scr.onkey(player.move_left, 'a')
scr.onkey(player.move_right, 'd')
scr.onkey(player.move_down, 's')
