from turtle import *

pensize(2)

def day():
    color('yellow')
    begin_fill()
    for i in range(18):
        forward(100)
        left(100)
    end_fill()

def night():
    color('bisque')
    begin_fill()
    circle(50)
    end_fill()


otvet = input('Какое сейчас время суток?')
if otvet == 'день':
    day()
if otvet == 'ночь':
    night()

exitonclick()
