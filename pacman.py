from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y):
        self.image = transform.scale(image.load(img), (70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

player = GameSprite('hero.png',100,100)
enemy = GameSprite('cyborg.png',300,100)

win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption('Лабиринт ужаса')

background = transform.scale(image.load('background3.png'), (win_width,win_height))

#музыка
#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0) )
    player.draw()
    enemy.draw()

    display.update()
    clock.tick(60)
