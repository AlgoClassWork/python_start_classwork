
from pygame import *
# создание экрана
window = display.set_mode( (700,500) )
display.set_caption('Арканойд')

# игровой цикл
clock = time.Clock()
game = True
while game:
    # обработка крестика
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False
    # заливка фона
    window.fill( (200,200,250) )

    # обновление кадров
    display.update()
    # настройка частоты кадров
    clock.tick(120)
