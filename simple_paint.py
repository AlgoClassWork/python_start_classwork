from turtle import *
from random import choice #new
#создание обьекта черепашки
picaso = Turtle()
picaso.width(5)
picaso.speed(3)
picaso.shape('circle')
picaso.colors = ['red','orange','yellow','green','lightblue','blue','purple'] # new
#создание обьекта экрана
screen = picaso.getscreen() 
screen.listen() 
#функционал
def draw(x,y):
    picaso.goto(x,y)

def move(x,y): 
    picaso.penup()
    picaso.goto(x,y)
    picaso.pendown()

def change_color(): #new
    color = choice(picaso.colors) 
    picaso.color(color)

#подписки на события
picaso.ondrag(draw)
screen.onscreenclick(move) 
screen.onkey(change_color,'c')  #new
