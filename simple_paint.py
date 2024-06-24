from turtle import *
#Создание и настройка черепахи
leonardo = Turtle()
leonardo.pensize(5)
leonardo.width(5)
leonardo.speed(15)
leonardo.shape('circle')
leonardo.pendown()
#Функционал редактора
def draw(x,y):
    leonardo.goto(x,y)
#Подписки на события
leonardo.ondrag(draw)

