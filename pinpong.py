from pygame import *

# Создание экрана размером 700 на 500 px
window = display.set_mode( (700,500) )
# Игровой цикл
game = True
while game:
    
    window.fill( (0,255,255) )

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
