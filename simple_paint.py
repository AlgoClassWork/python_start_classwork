from turtle import *
#Создание и настройка черепахи
leonardo = Turtle()
leonardo.pensize(5)
leonardo.width(5)
leonardo.speed(15)
leonardo.shape('circle')
leonardo.pendown()
#создаем обьект экрана
screen = leonardo.getscreen()
screen.listen()
#Функционал редактора
def draw(x,y):
    leonardo.goto(x,y)

def move(x,y):
    leonardo.penup()
    leonardo.goto(x,y)
    leonardo.pendown()

def set_red():
    leonardo.color('red')

def set_black():
    leonardo.color('black')

def step_right():
    #первый способ
    leonardo.goto(leonardo.xcor() + 5, leonardo.ycor())
    #второй способ
    #leonardo.setheading(0)
    #leonardo.forward(5)

def step_left():
    leonardo.goto(leonardo.xcor() - 5, leonardo.ycor())

#Подписки на события
leonardo.ondrag(draw)

screen.onscreenclick(move)
screen.onkey(set_red,'r')
screen.onkey(set_black,'b')
screen.onkey(step_right,'Right')
screen.onkey(step_left,'Left')
