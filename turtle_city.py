from turtle import *


# Земля
penup()
goto(-200, -200)
pendown()
color('yellowgreen')
begin_fill()
forward(400)
left(90)
forward(100)
left(90)
forward(400)
left(90)
forward(100)
left(90)
end_fill()


# Небо
penup()
goto(-200, -100)
pendown()
color('skyblue')
begin_fill()
forward(400)
left(90)
forward(300)
left(90)
forward(400)
left(90)
forward(300)
left(90)
end_fill()


# Солнце
penup()
goto(140, 140)
pendown()
begin_fill()
color('yellow')
for i in range(18):
       forward(40)
       left(100)
end_fill()


# Аптека
penup()
goto(120, -160)
pendown()
color('goldenrod')
begin_fill()
for i in range(3):
       forward(70)
       left(90)  
end_fill()
penup()
goto(140, -110)
pendown()
pensize(5)
color('red')
forward(15)
penup()
goto(150, -118)
pendown()
color('red')
right(90)
forward(20)




hideturtle()
exitonclick()
