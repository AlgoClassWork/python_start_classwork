from typing import Any
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img , x ,y):
        super().__init__()
        self.image = transform.scale(image.load(img),(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):

    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[K_s] and self.rect.y < 440:
            self.rect.y += 5
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[K_d] and self.rect.x < 640:
            self.rect.x += 5

class Enemy(GameSprite):

    def move(self):

        if self.rect.x <= 400:
            self.side = 'право'
        if self.rect.x >= 640:
            self.side = 'лево'

        if self.side == 'лево':
            self.rect.x -= 5
        else:
            self.rect.x += 5

player = Player('pica.png',300,300)
enemy = Enemy('adolf.png',350,200)
goal = GameSprite('suhar.png',600,400)

window = display.set_mode((700,500))
display.set_caption('ИГРА ЛАБИРИНТ')

background =  transform.scale(image.load('background.jpg'),(700,500))

#mixer.init()
#mixer.music.load('music.mp3')
#mixer.music.play()

clock = time.Clock()

game = True
while game:

    window.blit(background,(0,0))

    player.update()
    player.move()

    enemy.update()
    enemy.move()

    goal.update()

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()
