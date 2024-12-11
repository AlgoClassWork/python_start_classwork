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

hero = GameSprite(img='rocket.png', w=70, h=100, x=300, y=400)

hero_img = transform.scale(image.load('rocket.png'), (70,100))
hero_x = 300
hero_y = 400


enemy_img = transform.scale(image.load('ufo.png'), (100,70))
enemy_x = 300
enemy_y = 400

game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(back, (0,0))
    window.blit(hero_img, (hero_x, hero_y))
    window.blit(enemy_img, (enemy_x, enemy_y))

    keys = key.get_pressed()
    if keys[K_LEFT]:
        hero_x -= 5
    if keys[K_RIGHT]:
        hero_x += 5


    time.delay(10)
    display.update()
    

