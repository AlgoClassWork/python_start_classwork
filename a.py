from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,weight,height):
        self.image = transform.scale(image.load(img), (weight,height) )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    pass

player = GameSprite('rocket.png',200,200,70,100)
enemy = GameSprite('ufo.png',400,200,100,70)

window = display.set_mode( (700,500) )
display.set_caption('Шутер')

back = transform.scale(image.load('galaxy.jpg'), (700,500) )

game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(back, (0,0) )
    player.show()
    enemy.show()

    display.update()
