from pygame import *
from random import randint

#фоновая музыка
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')

#шрифты и надписи
font.init()
font2 = font.Font(None, 36)
font_end = font.Font(None, 150)
win_text = font_end.render('YOU WIN', 1, (0,255,0))
lose_text = font_end.render('YOU LOSE', 1, (255,0,0))


# нам нужны такие картинки:
img_back = "galaxy.jpg" # фон игры
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг

score = 0 # сбито кораблей
lost = 0 # пропущено кораблей
timer = 0 # таймер

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 20, 20, 20 )
        bullets.add(bullet)

class Bullet(GameSprite):
    
    def update(self):
        self.rect.y -= self.speed 

# класс спрайта-врага   
class Enemy(GameSprite):
    # движение врага
    def update(self):
        self.rect.y += self.speed
        global lost
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Boss(sprite.Sprite):
    def __init__(self, img, x, y):
        self.image = transform.scale(image.load(img), (200, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 10

    def reset(self):
        if timer > 10:
            window.blit(self.image, (self.rect.x, self.rect.y))
    
    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += 3
        else:
            self.rect.x -= 3

    def fire(self):
        global timer
        if int(timer) % 5 == 0:
            timer += 1
            bomb = Bullet('bullet.png', self.rect.centerx, self.rect.y, 50, 50, -5 )
            bombs.add(bomb)

# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# создаем спрайты
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
boss = Boss('boss.png', 300,50)

bullets = sprite.Group()
bombs = sprite.Group()

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:

    timer += 0.05
    
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
            if e.key == K_r:
                score = 0
                lost = 0
                finish = False

    if not finish:
        # обновляем фон
        window.blit(background,(0,0))

        # пишем текст на экране
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        # производим движения спрайтов
        ship.update()
        monsters.update()
        bullets.update()
        bombs.update()
        boss.update(ship)

        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        bombs.draw(window)
        boss.reset()

        boss.fire()

        if sprite.groupcollide(bullets, monsters, True, True):
            score += 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        if score > 50:
            window.blit(win_text,(100,200))
            finish = True

        if sprite.spritecollide(ship, monsters, True) or lost > 5:
            window.blit(lose_text,(100,200))
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
            finish = True


        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
