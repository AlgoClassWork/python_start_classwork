from turtle import *
#создание обьекта черепашки
picaso = Turtle()
picaso.width(5)
picaso.speed(3)
picaso.shape('circle')
#создание обьекта экрана
screen = picaso.getscreen() 
screen.listen() #new
#функционал
def draw(x,y):
    picaso.goto(x,y)

def move(x,y): 
    picaso.penup()
    picaso.goto(x,y)
    picaso.pendown()

def set_green(): # new
    picaso.color('green')

def set_red(): # new
    picaso.color('red')
#подписки на события
picaso.ondrag(draw)
screen.onscreenclick(move) 
screen.onkey(set_green,'g') # new
screen.onkey(set_red,'r') # new
