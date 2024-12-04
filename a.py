from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y):
        self.image = transform.scale(image.load(img),(70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0 :
            self.rect.y -= 5
        if keys[K_s] and self.rect.y < 430:
            self.rect.y += 5
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += 5

class Enemy(GameSprite):
    direction = 'left'
    def move(self, point_a, point_b):
        if self.rect.x > point_b:
            self.direction = 'left'
        if self.rect.x < point_a:
            self.direction = 'right'

        if self.direction == 'left':
            self.rect.x -= 5
        else:
            self.rect.x += 5

hero = Player(img='hero.png', x=200, y=200)
enemy = Enemy(img='cyborg.png', x=400, y=200)
enemy2 = Enemy(img='cyborg.png', x=600, y=400)

window = display.set_mode( (700,500) )
display.set_caption('Лабиринт')

background = transform.scale(image.load('background.jpg'), (700,500))

#музыка
#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

clock = time.Clock()
game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    hero.show()
    enemy.show()
    enemy2.show()

    hero.move()
    enemy.move(0,300)
    enemy2.move(300,600)

    if sprite.collide_rect(hero, enemy):
        print('Столкновение')

    display.update()
    clock.tick(60)
