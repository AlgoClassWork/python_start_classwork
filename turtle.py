from turtle import *
from random import randint

gitler = Turtle()
picachu = Turtle()

def start_race(turt,col,y):
   turt.color('black',col)
   turt.penup()
   turt.goto(-200,y)
   turt.shape('turtle')

start_race(turt=gitler,col='red',y=40)
start_race(turt=picachu,col='yellow',y=-40)

finish = 200
stavka = input('На кого вы хотите поставить?').lower()
while gitler.xcor() < finish and picachu.xcor() < finish:
   gitler.forward(randint(1,10))
   picachu.forward(randint(1,10))

winner = max(gitler.xcor(),picachu.xcor())
if winner == gitler.xcor():
   gitler.goto(-200,-20)
   if stavka == 'гитлер':
      gitler.write('Ты выйграл пачку сухариков',font=('Arial',22,'bold'))
   else:
      gitler.write('Твой дом заберут коллекторы',font=('Arial',22,'bold'))
else:
   picachu.goto(-200,-20)
   if stavka == 'пикачу':
      picachu.write('Ты выйграл пачку сухариков',font=('Arial',22,'bold'))
   else:
      picachu.write('Твой дом заберут коллекторы',font=('Arial',22,'bold'))

gitler.hideturtle()
picachu.hideturtle()


