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

class Wall(sprite.Sprite):
    def __init__(self, width, height, x, y):
        self.image = Surface((width,height))
        self.image.fill((60,220,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall = Wall(width=10, height=350, x=150, y=150 )
wall2 = Wall(width=450, height=10, x=150, y=150 )
wall3 = Wall(width=450, height=10, x=300, y=300 )


hero = Player(img='hero.png', x=0, y=400)
enemy = Enemy(img='cyborg.png', x=400, y=200)
enemy2 = Enemy(img='cyborg.png', x=600, y=400)
gold = GameSprite(img='treasure.png', x=400, y=400)

window = display.set_mode( (700,500) )
display.set_caption('Лабиринт')

background = transform.scale(image.load('background.jpg'), (700,500))

#музыка
#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

#надписи
font.init()
my_font = font.Font(None,120)
win_text = my_font.render('ПОБЕДА', True, (0,255,0))
lose_text = my_font.render('ПРОИГРЫШ', True, (255,0,0))

clock = time.Clock()
finish = False
game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    keys = key.get_pressed()
    if keys[K_r]:
        finish = False
        hero.rect.x = 0
        hero.rect.y = 400

    if not finish:
        window.blit(background, (0, 0))

        hero.show()
        enemy.show()
        enemy2.show()
        gold.show()

        wall.show()
        wall2.show()
        wall3.show()
        
        hero.move()
        enemy.move(0,300)
        enemy2.move(300,600)

        walls = [wall, wall2, wall3]
        for some_wall in walls:
            if sprite.collide_rect(hero, some_wall):
                hero.rect.x = 0
                hero.rect.y = 400
        
        if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, enemy2):
            window.blit(lose_text,(100,200))
            finish = True

        if sprite.collide_rect(hero, gold):
            window.blit(win_text,(100,200))
            finish = True

        display.update()

    clock.tick(60)
