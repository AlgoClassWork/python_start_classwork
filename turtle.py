from turtle import *

def svetofor(wich_color_on):

    penup()
    goto(0,110)
    pendown()
    color('red')
    if wich_color_on.find('красный') != -1:
        begin_fill()
        circle(50)
        end_fill()
    else:
        circle(50)

    penup()
    goto(0,0)
    pendown()
    color('yellow')
    if wich_color_on.find('желтый') != -1:
        begin_fill()
        circle(50)
        end_fill()
    else:
        circle(50)

    penup()
    goto(0,-110)
    pendown()
    color('green')
    if wich_color_on == 'зеленый':
        begin_fill()
        circle(50)
        end_fill()
    else:
        circle(50)

otvet = input('Какой свет сейчас горит?')
svetofor(otvet)
exitonclick()
