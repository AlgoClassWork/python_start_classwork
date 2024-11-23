from pygame import *
#создаем экран
window = display.set_mode( (700,500) )
display.set_caption('Догонялки')
#загрузка игровых картинок
background = image.load('back.png')
background = transform.scale(background, (700,500))
#запускаем игровой цикл
game = True
while game:
    #отображение картинок
    window.blit(background, (0,0) )
    #обрабатываем нажатие на крестик
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
