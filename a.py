from pygame import *

# Создание и настройка экрана
window = display.set_mode((700,500))
display.set_caption('Шутер')
back = transform.scale(image.load('galaxy.jpg'), (700,500))
# Игровые переменные
game = True
# Игровой цикл
while game:
    # Обработка выхода из игры
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False
    # Отображение обьектов
    window.blit(back, (0,0))

    display.update()
