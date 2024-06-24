from turtle import *
# Создание и настройка обьекта черепашки
picaso = Turtle()
picaso.width(5)
picaso.speed(10)
picaso.shape('circle')
# Cоздание и настройка обьекта экрана
screen = picaso.getscreen()
# Функционал редактора
def draw(x,y):
    picaso.goto(x,y)
    
def move(x,y):
    picaso.penup()
    picaso.goto(x,y)
    picaso.pendown()
# Подписки на события
picaso.ondrag(draw)
screen.onscreenclick(move)
