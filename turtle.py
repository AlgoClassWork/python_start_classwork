from turtle import *
 
def fence_link(col):
    pensize(2)
    color("black",col)
    begin_fill()
    left(90)
    forward(100)
    right(30)
    forward(42)
    right(120)
    forward(42)
    right(30)
    forward(100)
    right(90)
    forward(42)
    left(180)
    end_fill()

    forward(42)


goto(-100,-50)
#допиши программу
otvet = input('Введи корпус: главный\приемная')
if otvet == 'главный':
    for i in range(3):
        fence_link('blue')

if otvet == 'приемная':
    for i in range(4):
        fence_link('green')


hideturtle()
exitonclick()







from turtle import *

def svetofor(col):

    color('red')
    goto(0,70)
    if col == 'красный':
        begin_fill()
    circle(30)
    if col == 'красный':
        end_fill()

    color('yellow')
    goto(0,0)
    if col == 'желтый':
        begin_fill()
    circle(30)
    if col == 'желтый':
        end_fill()

    color('green')
    goto(0,-70)
    if col == 'зеленый':
        begin_fill()
    circle(30)
    if col == 'зеленый':
        end_fill()

otvet = input('Какой свет сейчас горит?')
if otvet == 'красный':
    svetofor(otvet)
if otvet == 'желтый':
    svetofor(otvet)
if otvet == 'зеленый':
    svetofor(otvet)

exitonclick()
