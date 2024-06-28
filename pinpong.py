from typing import Any
from pygame import *
# Описываем наших персонажей
class GameSprite(sprite.Sprite):
    def __init__(self,x,y,img):
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

# Создание игровых обьектов
ball = GameSprite(x=350,y=250,img='tenis_ball.png')
raketka1 = GameSprite(x=0,y=250,img='racket.png')
raketka2 = GameSprite(x=650,y=250,img='racket.png')

# Создание экрана размером 700 на 500 px
window = display.set_mode( (700,500) )

score_player = 0
score_ai = 0

font.init()

player = font.Font(None,40).render('Счет: '+str(score_player),True,(255,255,255))
ai = font.Font(None,40).render('Счет: '+str(score_ai),True,(255,255,255))

speed_x = 1
speed_y = 1
# Игровой цикл
game = True
while game:
    
    window.fill( (0,255,255) )
    window.blit(player,(20,20))
    window.blit(player,(580,20))
    ball.update()
    raketka1.update()
    raketka2.update()

    for e in event.get():
        if e.type == QUIT:
            game = False

    mouse_x, mouse_y = mouse.get_pos()
    raketka1.rect.centery = mouse_y

    if ball.rect.centery > raketka2.rect.centery:
        raketka2.rect.y += 1
    else:
        raketka2.rect.y -= 1

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(ball,raketka1) or sprite.collide_rect(ball,raketka2):
        speed_x *= -1

    
    time.delay(1)
    display.update()
