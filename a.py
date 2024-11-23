from pygame import *
#создаем экран
window = display.set_mode( (700,500) )
display.set_caption('Догонялки')
#загрузка игровых картинок
background = image.load('back.png')
background = transform.scale(background, (700,500))

pica = transform.scale(image.load('pica.png'), (100,100))
gita = transform.scale(image.load('gita.png'), (100,100))
#запускаем игровой цикл
game = True
while game:
    #отображение картинок
    window.blit(background, (0,0) )
    window.blit(pica, (100,100) )
    window.blit(gita, (300,100) )
    #обрабатываем нажатие на крестик
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
