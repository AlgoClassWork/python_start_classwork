from turtle import *
from random import choice 
#создание обьекта черепашки
picaso = Turtle()
picaso.width(5)
picaso.speed(3)
picaso.shape('circle')
picaso.colors = ['red','orange','yellow','green','lightblue','blue','purple'] 
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

def change_color(): 
    color = choice(picaso.colors) 
    picaso.color(color)

def go_up(): #new
    picaso.goto(picaso.xcor(),picaso.ycor()+5)

def go_left(): #new
    picaso.goto(picaso.xcor()-5,picaso.ycor())

def go_down(): #new
    picaso.goto(picaso.xcor(),picaso.ycor()-5)

def go_right(): #new
    picaso.goto(picaso.xcor()+5,picaso.ycor())

#подписки на события
picaso.ondrag(draw)
screen.onscreenclick(move) 
screen.onkey(change_color,'c')  
screen.onkey(go_up,'w') #new
screen.onkey(go_left,'a') #new
screen.onkey(go_down,'s') #new
screen.onkey(go_right,'d') #new
