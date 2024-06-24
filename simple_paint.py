from turtle import *
# Создание и настройка обьекта черепашки
picaso = Turtle()
picaso.width(5)
picaso.speed(10)
picaso.shape('circle')
picaso.size = 1
# Cоздание и настройка обьекта экрана
screen = picaso.getscreen()
screen.listen()
# Функционал редактора
def draw(x,y):
    picaso.goto(x,y)
    
def move(x,y):
    picaso.penup()
    picaso.goto(x,y)
    picaso.pendown()

def set_red():
    picaso.color('black','red')

def set_black():
    picaso.color('black','black')

def up_line():
    picaso.goto(picaso.xcor(),picaso.ycor() + 5)

def down_line():
    picaso.goto(picaso.xcor(),picaso.ycor() -5)

def right_line():
    picaso.goto(picaso.xcor()  + 5,picaso.ycor())

def left_line():
    picaso.goto(picaso.xcor()  - 5,picaso.ycor())

def start_fill():
    picaso.begin_fill()

def finish_fill():
    picaso.end_fill()

def pensize_plus():
    picaso.pensize(picaso.size)
    picaso.size += 1
# Подписки на события
picaso.ondrag(draw)
screen.onscreenclick(move)

screen.onkey(set_red,'r')
screen.onkey(set_black,'b')
screen.onkey(up_line,'Up')
screen.onkey(down_line,'Downr')
screen.onkey(right_line,'Right')
screen.onkey(left_line,'Left')
screen.onkey(start_fill,'s')
screen.onkey(finish_fill,'f')
screen.onkey(pensize_plus,'q')
