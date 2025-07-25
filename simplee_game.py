from pygame import *
# Создание экрана для игры
window = display.set_mode( (700, 500) )
# Загрузка картинки для игры
background = image.load('back.jpg')
background = transform.scale(background, (700, 500) )
# Загрузка картинки для персонажа
pica = image.load('pica.png')
pica = transform.scale(pica, (150, 150) )
pica_x, pica_y = 200, 200
# Игровой цикл
while True:
    # Обработка нажатия на крестик
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    keys = key.get_pressed()
    if keys[K_w] and pica_y > -50:
        pica_y -= 1
    if keys[K_s] and pica_y < 400:
        pica_y += 1
    if keys[K_a] and pica_x > -50:
        pica_x -= 1
    if keys[K_d] and pica_x < 600:
        pica_x += 1
    # Отображение картинок
    window.blit(background, (0, 0) )
    window.blit(pica, (pica_x, pica_y) )
    # Обновление кадров игры
    display.update()
