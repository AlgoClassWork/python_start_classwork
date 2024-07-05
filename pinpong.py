from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img ,cord_x ,cord_y ,width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
        self.speed = speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

player = GameSprite('platform.png',0,200,20,200,10)
enemy = GameSprite('enemy.png',650,200,50,200,10)
ball = GameSprite('ball.png',300,200,70,70,10)

window = display.set_mode((700,500))
display.set_caption('ПЕНГ-ПУНГ')

clock = time.Clock()

finish = False
game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        window.fill( (255,255,255) )

        player.reset()
        enemy.reset()
        ball.reset()


    clock.tick(60)
    display.update()
