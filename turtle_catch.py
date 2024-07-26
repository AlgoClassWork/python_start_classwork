from turtle import *
from random import randint
from time import sleep, time

naruto = Turtle()
naruto.shape('turtle')
naruto.color('black','orange')
naruto.speed(10)
naruto.penup()
naruto.points = 0 

def rand_move():
    naruto.goto(randint(-200,200),randint(-200,200))

def catch(x,y):
    naruto.write('Ай',font=('Arial',15,'bold'))
    naruto.points += 1
    rand_move() 

start = time() #new

naruto.onclick(catch)
while naruto.points < 3: 
    rand_move()
    sleep(1)

end = time() #new
total = str(int(end-start)) + ' c' #new

naruto.clear() 
naruto.goto(-150,0) 
naruto.write('Ты победил за ' + total ,font=('Arial',30,'bold')) #new
naruto.hideturtle() 
