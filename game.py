from pygame import *
# Создание экрана
window = display.set_mode( (700,500) )
display.set_caption('Догонялки')
# Загрузка картинки для заднего фона
background = image.load('fon.png')
background = transform.scale(background, (700,500))

pica = image.load('pica.png') # NEW
pica = transform.scale(pica, (80,120)) # NEW
# Игровой цикл
game = True
while game:
    # Обработка нажатия на крестик
    for e in event.get():
        if e.type == QUIT:
            game = False
    # Отображение картинок
    window.blit( background, (0,0) )
    window.blit(pica, (200,200)) # NEW
    display.update()
