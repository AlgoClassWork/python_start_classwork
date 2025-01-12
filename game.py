from pygame import *
# Создание экрана
window = display.set_mode( (700,500) )
display.set_caption('Догонялки')
# Загрузка картинки для заднего фона
background = image.load('fon.png')
background = transform.scale(background, (700,500))

pica = image.load('pica.png') 
pica = transform.scale(pica, (80,120)) 
pica_x, pica_y = 200, 200 
# Игровой цикл
game = True
while game:
    # Обработка нажатия на крестик
    for e in event.get():
        if e.type == QUIT:
            game = False
    # Отображение картинок
    window.blit( background, (0,0) )
    window.blit( pica, (pica_x, pica_y) ) 
    # Движение персонажей
    keys = key.get_pressed()
    if keys[K_w] and pica_y > 0:
        pica_y -= 1
    if keys[K_s] and pica_y < 250:
        pica_y += 1
    if keys[K_a] and pica_x > 0:
        pica_x -= 1
    if keys[K_d] and pica_x < 600:
        pica_x += 1

    display.update()
