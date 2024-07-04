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

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(sprite_img='bullet.png',cord_x=self.rect.centerx,cord_y=self.rect.top,width=20,height=20,speed=20)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,600)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

player = Player(sprite_img='rocket.png',cord_x=300,cord_y=400,width=70,height=100,speed=15)

bullets = sprite.Group()

enemys = sprite.Group()
for _ in range(5):
    enemy = Enemy(sprite_img='ufo.png',cord_x=randint(0,600),cord_y=0,width=100,height=50,speed=randint(1,3)) 
    enemys.add(enemy)

window = display.set_mode((700,500))
display.set_caption('КОСМИЧЕСКИЙ ШУТЕР')

background =  transform.scale(image.load('galaxy.jpg'),(700,500))

#mixer.init()
#mixer.music.load('music.mp3')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.mp3')

font.init()
font1 = font.Font(None,35)
font2 = font.Font(None,120)

score = 0
lost = 0

clock = time.Clock()

finish = False
game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                #fire_sound.play()
                player.fire()

    if finish != True:

        window.blit(background,(0,0))

        player.reset()
        player.move()

        enemys.draw(window)
        enemys.update()

        bullets.draw(window)
        bullets.update()

        score_label = font1.render('Убито:' + str(score),1,(255,255,0))
        lost_label = font1.render('Пропущено:' + str(lost),1,(255,255,0))

        window.blit(score_label,(10,10))
        window.blit(lost_label,(10,40))

        if sprite.groupcollide(enemys,bullets,True,True):
            score += 1
            enemy = Enemy(sprite_img='ufo.png',cord_x=randint(0,600),cord_y=0,width=100,height=50,speed=randint(1,3)) 
            enemys.add(enemy)

        if lost > 5:
            lose = font2.render('ТЫ ПРОИГРАЛ',1,(255,0,0))
            window.blit(lose,(100,250))
            finish = True

        if score > 15:
            win = font2.render('ТЫ ПОБЕДИЛ',1,(0,255,0))
            window.blit(win,(100,250))
            finish = True

    clock.tick(60)
    display.update()
