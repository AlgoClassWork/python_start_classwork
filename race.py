from turtle import *
from random import randint

pica = Turtle()
adolf = Turtle()

def start_race(name,col,cord_y):
   name.color('black',col)
   name.shape('turtle')
   name.penup()
   name.goto(-200,cord_y)

start_race(name=pica,col='yellow',cord_y=50)
start_race(name=adolf,col='black',cord_y=-50)

while pica.xcor() < 200 and adolf.xcor() < 200:
   pica.forward( randint(1,20) )
   adolf.forward( randint(1,20) )

if adolf.xcor() > pica.xcor():
   adolf.goto(-200,0)
   adolf.write('ПОБЕДА АДОЛЬФА',font=('Arial',35,'bold'))
else:
   pica.goto(-200,0)
   pica.write('ПОБЕДА ПИКАЧУ',font=('Arial',35,'bold'))

adolf.hideturtle()
pica.hideturtle()
