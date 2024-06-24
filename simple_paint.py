from turtle import *
# Создание и настройка обьекта черепашки
picaso = Turtle()
picaso.width(5)
picaso.speed(10)
picaso.shape('circle')
# Функционал редактора
def draw(x,y):
    picaso.goto(x,y)
# Подписки на события
picaso.ondrag(draw)
