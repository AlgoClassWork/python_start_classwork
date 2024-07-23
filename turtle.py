from turtle import *

pensize(2)
goto(-50,-50)

begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()

penup()
goto(170,-50)
pendown()

circle(3)

exitonclick()
