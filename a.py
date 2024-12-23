from random import randint
from pygame import *

lost = 0
score = 0
boss_health = 10

font.init()
count_font = font.Font(None,30)
final_font = font.Font(None,150)


# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx + 10, 400,20,40,20 )
        bullets.add(bullet)
        bullet = Bullet('bullet.png',self.rect.centerx - 30, 400,20,40,20 )
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed


# класс для врагов
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            lost += 1
            self.rect.y = 0
            self.rect.x = randint(0,600)

class Boss(GameSprite):
    def update(self):
        if self.rect.centerx > ship.rect.centerx:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def attack(self):
        global timer
        if int(timer) % 3 == 0:
            timer += 1
            meteor = Bullet('asteroid.png',self.rect.centerx, 100, 50, 50, -5)
            enemys.add(meteor)

# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

# создаем спрайты
ship = Player('rocket.png', 5, win_height - 100, 80, 100, 10)

bullets = sprite.Group()

enemys = sprite.Group()

for i in range(5):
    enemy = Enemy('ufo.png',randint(0,600),0,100,50,randint(1,5))
    enemys.add(enemy)

boss = Boss('boss.png', 250, 50, 200, 100, 3)

# Основной цикл игры:
run = True 
finish = False
timer = 0

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
            elif e.key == K_r:
                timer = 0
                boss_health = 0
                lost = 0
                score = 0
                finish = False

    timer += 0.03

    if not finish:
        window.blit(background, (0,0))

        lost_text = count_font.render(f'Пропущено: {lost}',1, (255,255,255))
        window.blit(lost_text, (10,10))

        score_text = count_font.render(f'Убито: {score}',1, (255,255,255))
        window.blit(score_text, (10,40))

        ship.update()
        enemys.update()
        boss.update()

        ship.show()

        if timer > 5:
            boss.attack()
            boss.show()

        enemys.draw(window)

        bullets.update()
        bullets.draw(window)

        hp = count_font.render(f'hp:{boss_health}',1, (255,255,255))
        window.blit(hp, (boss.rect.centerx, 0 ))

        
        if sprite.groupcollide(bullets, enemys, True, True ):
            enemy = Enemy('ufo.png',randint(0,600),0,100,50,randint(1,5))
            enemys.add(enemy)
            score += 1
            
        if sprite.spritecollide(ship, enemys, True):
            lose_text = final_font.render('LOSE',1, (255,255,255))
            window.blit(lose_text, (200,200))

            enemy = Enemy('ufo.png',randint(0,600),0,100,50,randint(1,5))
            enemys.add(enemy)

            finish = True
        
        if sprite.spritecollide(boss, bullets, True) and timer > 5:
            boss_health -= 1

        if score > 30 or boss_health < 0:
            win_text = final_font.render('WIN',1, (255,255,255))
            window.blit(win_text, (250,200))
            finish = True

        display.update()

    time.delay(30)
