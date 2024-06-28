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

# Игровой цикл
game = True
while game:
    
    window.fill( (0,255,255) )
    ball.update()
    raketka1.update()
    raketka2.update()

    for e in event.get():
        if e.type == QUIT:
            game = False

    mouse_x, mouse_y = mouse.get_pos()
    raketka1.rect.centery = mouse_y
    

    display.update()
