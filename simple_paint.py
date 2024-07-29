from turtle import *
#создание обьекта черепашки
picaso = Turtle()
picaso.width(10)
picaso.speed(10)
picaso.shape('circle')
#создание обьекта экрана
screen = picaso.getscreen() #new
#функционал
def draw(x,y):
    picaso.goto(x,y)

def move(x,y): # new
    picaso.penup()
    picaso.goto(x,y)
    picaso.pendown()
#подписки на события
picaso.ondrag(draw)
screen.onscreenclick(move) #new
