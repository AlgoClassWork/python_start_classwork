from pygame import *
# Создание экрана
window = display.set_mode( (700,500) )
display.set_caption('Догонялки')
# Загрузка картинки для заднего фона
background = image.load('fon.png')
background = transform.scale(background, (700,500))

pica = image.load('pica.png') 
pica = transform.scale(pica, (80,120)) 
pica_x, pica_y = 0, 100 

ball = image.load('ball.png') 
ball = transform.scale(ball, (50,50)) 
ball_x, ball_y = 300, 150 
speed_x, speed_y = 1, 1
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
    window.blit( ball, (ball_x, ball_y) )
    # Движение персонажей
    keys = key.get_pressed()
    if keys[K_w] and pica_y > 0:
        pica_y -= 1
    if keys[K_s] and pica_y < 250:
        pica_y += 1

    ball_x += speed_x
    ball_y += speed_y

    if ball_x > 650 or ball_x < 0:
        speed_x *= -1
    if ball_y > 350 or ball_y < 0:
        speed_y *= -1

    display.update()
