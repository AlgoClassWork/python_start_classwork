from turtle import *
# Создание и настройка обьекта черепашки
picaso = Turtle()
picaso.width(5)
picaso.speed(10)
picaso.shape('circle')
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
    picaso.color('red')

def set_black():
    picaso.color('black')
# Подписки на события
picaso.ondrag(draw)
screen.onscreenclick(move)

screen.onkey(set_red,'r')
screen.onkey(set_black,'b')
