from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))

player = GameSprite('platform.png',10,200,10,100)
ai = GameSprite('platform.png',680,200,10,100)
ball = GameSprite('ball.png',325,225,50,50)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill((255,255,255))

    player.show()
    ai.show()
    ball.show()

    display.update()
