from turtle import *

def svetofor(svet):
    goto(0,90)
    color('red')
    if svet.find('красный') != -1:
        begin_fill()
        circle(30)
        end_fill()
    else:
        circle(30)

    goto(0,0)
    color('yellow')
    if svet.find('желтый') != -1:
        begin_fill()
        circle(30)
        end_fill()
    else:
        circle(30)

    goto(0,-90)
    color('green')
    if svet.find('зеленый') != -1:
        begin_fill()
        circle(30)
        end_fill()
    else:
        circle(30)

otvet = input('Какой сейчас горит свет')
svetofor(otvet)

exitonclick()
