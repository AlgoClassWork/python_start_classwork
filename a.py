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
        if keys[K_w]:
            self.rect.y -= 5
        if keys[K_s]:
            self.rect.y += 5
        if keys[K_a]:
            self.rect.x -= 5
        if keys[K_d]:
            self.rect.x += 5
    
hero = Player(img='hero.png', x=200, y=200)
enemy = GameSprite(img='cyborg.png', x=400, y=200)

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

    hero.move()

    if sprite.collide_rect(hero, enemy):
        print('Столкновение')

    display.update()
    clock.tick(60)
