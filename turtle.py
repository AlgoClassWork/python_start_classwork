from turtle import *
 
def fence_link():
    pensize(2)
    color("black","orange")
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

for i in range(6):
    fence_link()
    forward(42)

hideturtle()
exitonclick()
