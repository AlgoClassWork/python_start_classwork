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
goto(150, 200)
color('yellow')
begin_fill()
for i in range(18):
    forward(100)
    right(100)
end_fill()

# Основание домика
penup()
goto(-250, -100)
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
penup()
goto(-250, -100)
pendown()
color('red')
begin_fill()
forward(200)
left(120)
forward(50)
left(60)
forward(150)
end_fill()

# Окно домика
penup()
goto(-180, -150)
pendown()
color('white')
begin_fill()
for i in range(4):
    forward(30)
    right(90)
end_fill()

# Дверь домика
penup()
goto(-100, -200)
pendown()
color('brown')
begin_fill()
for i in range(2):
    forward(40)
    right(90)
    forward(60)
    right(90)
end_fill()

# Дерево 
penup()
goto(50, -100)
pendown()
color('brown')
begin_fill()
for i in range(2):
    forward(20)
    right(90)
    forward(50)
    right(90)
end_fill()

penup()
goto(65, -60)
pendown()
color('green')
begin_fill()
for i in range(3):
    forward(50)
    right(120)
end_fill()

penup()
goto(65, -30)
pendown()
color('green')
begin_fill()
for i in range(3):
    forward(50)
    right(120)
end_fill()

# Дерево 2
penup()
goto(150, -150)
pendown()
color('brown')
begin_fill()
for i in range(2):
    forward(20)
    right(90)
    forward(50)
    right(90)
end_fill()

penup()
goto(165, -110)
pendown()
color('green')
begin_fill()
for i in range(3):
    forward(50)
    right(120)
end_fill()

penup()
goto(165, -80)
pendown()
color('green')
begin_fill()
for i in range(3):
    forward(50)
    right(120)
end_fill()


hideturtle()
exitonclick()
