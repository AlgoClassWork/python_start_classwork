# pip install pygame
from pygame import *
# Создание экрана для игры
window = display.set_mode(size=(700,500))
display.set_caption('Догонялки')

background = image.load('background.jpg')
background = transform.scale(background, (700,500))

enemy = transform.scale(image.load('enemy.png'), (100,100))
enemy_x = 0
enemy_y = 0

player = transform.scale(image.load('player.png'), (100,100))
player_x = 0
player_y = 0

# Игровой цикл
clock = time.Clock()
while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    window.blit(background, (0, 0))
    window.blit(enemy, (enemy_x, enemy_y))
    window.blit(player, (player_x, player_y))

    keys = key.get_pressed() 
    if keys[K_d] and enemy_x < 600:
        enemy_x += 10
    if keys[K_a] and enemy_x > 0:
        enemy_x -= 10
    if keys[K_w] and enemy_y > 0:
        enemy_y -= 10
    if keys[K_s] and enemy_y < 400:
        enemy_y += 10

    if enemy_x > player_x:
        player_x += 5
    if enemy_x < player_x:
        player_x -= 5
    if enemy_y > player_y:
        player_y += 5
    if enemy_y < player_y:
        player_y -= 5

    display.update()
    clock.tick(60)
