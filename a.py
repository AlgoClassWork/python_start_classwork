from pygame import *

window = display.set_mode( (700,500) )
display.set_caption('Космический шутер')

back = transform.scale(image.load('galaxy.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,w,h):
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.rect.x += 5

hero = Player(img='rocket.png', w=70, h=100, x=300, y=400)

game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(back, (0,0))
    hero.show()
    hero.move()

    time.delay(10)
    display.update()
    

