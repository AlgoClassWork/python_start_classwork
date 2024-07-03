from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img ,cord_x ,cord_y ,width, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += 5

player = Player(sprite_img='rocket.png',cord_x=300,cord_y=400,width=70,height=100)

window = display.set_mode((700,500))
display.set_caption('КОСМИЧЕСКИЙ ШУТЕР')

background =  transform.scale(image.load('galaxy.jpg'),(700,500))

#mixer.init()
#mixer.music.load('music.mp3')
#mixer.music.play()

clock = time.Clock()

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))

    player.reset()
    player.move()

    clock.tick(60)
    display.update()
