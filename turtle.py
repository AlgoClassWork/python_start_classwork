from turtle import *
from random import randint

def start_race(name,col,y):
   name.penup()
   name.goto(-200,y)
   name.shape('turtle')
   name.color('black',col)

biba = Turtle()
boba = Turtle()

start_race(name=biba,col='red',y=40)
start_race(name=boba,col='blue',y=-40)

finish = 200

stavka = input('Кто победит?').lower()

while biba.xcor() < finish and boba.xcor() < finish:
   biba.forward( randint(1,10) )
   boba.forward( randint(1,10) )

winner = max(biba.xcor(), boba.xcor())

if biba.xcor() == winner:
   biba.goto(-200,-20)
   if stavka == 'биба':
      biba.write('Вы выйграли пачку сухариков',font=('Arial',20,'bold'))
   else:
      biba.write('Вы проиграли :(',font=('Arial',20,'bold'))

if boba.xcor() == winner:
   boba.goto(-200,-20)
   if stavka == 'боба':
      boba.write('Вы выйграли пачку сухариков',font=('Arial',20,'bold'))
   else:
      boba.write('Вы проиграли :(',font=('Arial',20,'bold'))

biba.hideturtle()
boba.hideturtle()
