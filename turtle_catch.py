from turtle import *
from random import randint
from time import sleep

naruto = Turtle()
naruto.shape('turtle')
naruto.color('black','orange')
naruto.speed(10)
naruto.penup()
# Определи функцию rand_move(), переносящую черепашку в случайную точку
def rand_move():
    naruto.goto(randint(-200,200),randint(-200,200))
# Определи функцию-обработчик catch(x, y), которая обработает клик по черепашке 
# (успешные клики копятся в свойстве t.points)
# Создай подписку на событие «клик по объекту-черепашке»
# Создай цикл, работающий пока кликов t.points меньше 3
while True:
    rand_move()
    sleep(1)
