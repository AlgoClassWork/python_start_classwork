from turtle import *

pica = Turtle()
adolf = Turtle()

def start_race(name,col,cord_y):
   name.color('black',col)
   name.shape('turtle')
   name.penup()
   name.goto(-200,cord_y)

start_race(name=pica,col='yellow',cord_y=50)
start_race(name=adolf,col='white',cord_y=-50)
