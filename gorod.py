from turtle import *

speed(100)

# земля
goto(-300, -100)
color('lightgreen')
begin_fill()
for i in range(2):
    forward(600)
    right(90)
    forward(200)
    right(90)
end_fill()

# небо
goto(-300, 300)
color('lightblue')
begin_fill()
for i in range(2):
    forward(600)
    right(90)
    forward(400)
    right(90)
end_fill()

# Солнышко
goto(200, 300)
color('yellow')
begin_fill()
for i in range(18):
    forward(100)
    right(100)
end_fill()

# Основание домика
penup()
goto(-250, -50)
pendown()
color('gray')
begin_fill()
for i in range(2):
    forward(200)
    right(90)
    forward(100)
    right(90)
end_fill()

# Крыша домика


exitonclick()
