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

#допиши программу
penup()
goto(-150,0)
pendown()

otvet = input('Что отрисовать приемную или главный корпус ')
if otvet == 'приемная':
    for i in range(4):
        fence_link('green')
        forward(42)
if otvet == 'главный корпус':
    for i in range(3):
        fence_link('blue')
        forward(42)


hideturtle()
exitonclick()
