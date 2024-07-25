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
start_race(name=adolf,col='white',cord_y=-50)

while pica.xcor() < 200 and adolf.xcor() < 200:
   pica.forward( randint(1,20) )
   adolf.forward( randint(1,20) )

if adolf.xcor() > pica.xcor():
   print('победил адольф')
else:
   print('победил пикачу')
