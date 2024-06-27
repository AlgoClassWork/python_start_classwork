from turtle import *
# Описываем наших персонажей
class Sprite(Turtle):
    def __init__(self,col,forma,x,y,naapravlenie):
        super().__init__()
        self.penup()
        self.color('black',col)
        self.shape(forma)
        self.goto(x,y)
        self.setheading(naapravlenie)

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

    def collide(self,turtle):
        dist = self.distance(turtle.xcor(),turtle.ycor())
        if dist < 30:
            return True
        else:
            return False
            

# Создаем наших игровых персонажей
player = Sprite(x=0,y=-150,forma='turtle',col='yellow',naapravlenie=90)
enemy1 = Sprite(x=150,y=50,forma='square',col='red',naapravlenie=180)
enemy2 = Sprite(x=-150,y=-50,forma='square',col='red',naapravlenie=0)
goal = Sprite(x=0,y=150,forma='triangle',col='green',naapravlenie=270)
# Создаем обьект экрана
screen = player.getscreen()
screen.listen()
# Подписки на события клавиатуры
screen.onkey(player.move_up,'Up')
screen.onkey(player.move_down,'Down')
screen.onkey(player.move_left,'Left')
screen.onkey(player.move_right,'Right')


while True:
    if player.collide(goal):
        goal.write('WIN',font=('Arial',25,'bold'))

        goal.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        player.hideturtle()

    if player.collide(enemy1) or player.collide(enemy2):
        enemy2.write('LOSE',font=('Arial',25,'bold'))

        goal.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        player.hideturtle()

    for i in range(50):
        enemy1.forward(5)
        enemy2.forward(5)

    enemy1.left(180)
    enemy2.left(180)






