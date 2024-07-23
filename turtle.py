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


from turtle import *

def square(col,size):
    color(col)
    begin_fill()
    for i in range(4):
        forward(size)
        left(90)
    end_fill()

square('black',200)
square('white',150)
square('lavender',100)
square('black',50)

exitonclick()
