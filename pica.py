from pygame import *
# Создаем экран
window = display.set_mode( (700,500) )
display.set_caption('Догонялки')
# Загрузка и изменения масштаба картинки
background = image.load('fon.jpg')
background = transform.scale(background,(700,500))

gita = transform.scale(image.load('гита.png'),(100,100))
pica = transform.scale(image.load('пика.png'),(100,100))

gita_x = 200
gita_y = 200

pica_x = 400
pica_y = 200
# Создаем игровой цикл
game = True
while game:
    # Отображение изображения
    window.blit(background,(0,0))
    window.blit(gita,(gita_x,gita_y))
    window.blit(pica,(pica_x,pica_y))
    # Обработка события нажатия на крестик для выхода
    for sobytie in event.get():
        if sobytie.type == QUIT:
            game = False
    # Получаем состояние клавиш
    keys_pressed = key.get_pressed()
    # Обработка нажатия W A S D
    if keys_pressed[K_w] and pica_y > 0:
        pica_y -= 1
    if keys_pressed[K_s] and pica_y < 400:
        pica_y += 1
    if keys_pressed[K_a] and pica_x > 0:
        pica_x -= 1
    if keys_pressed[K_d] and pica_x < 600:
        pica_x += 1
    # Обновление кадров на нашем экране
    display.update()
