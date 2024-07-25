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

winner = input('Кто победит?').lower()

while pica.xcor() < 200 and adolf.xcor() < 200:
   pica.forward( randint(1,20) )
   adolf.forward( randint(1,20) )

if adolf.xcor() > pica.xcor():
   adolf.goto(-200,0)
   if winner == 'адольф':
      adolf.write('Вы выйграли пачку сухариков',font=('Arial',20,'bold'))
   else:
      adolf.write('Ваш дом заберут коллекторы',font=('Arial',20,'bold'))
else:
   pica.goto(-200,0)
   if winner == 'пикачу':
      pica.write('Вы выйграли пачку сухариков',font=('Arial',20,'bold'))
   else:
      pica.write('Ваш дом заберут коллекторы',font=('Arial',20,'bold'))

adolf.hideturtle()
pica.hideturtle()
