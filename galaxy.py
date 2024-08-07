from pygame import *
from random import randint

# фоновая музыка


# шрифты и надписи
font.init()
font_for_score = font.Font('game_font.ttf',40)
font_end_game = font.Font('game_font.ttf',100)
win_text = font_end_game.render('YOU WIN',1,(0,255,0))
lose_text = font_end_game.render('YOU LOSE',1,(255,0,0))

# нам нужны такие картинки:
img_back = "back.jpg" # фон игры
img_hero = "player.png" # герой
img_enemy = "enemy.png" # враг
img_bullet = 'bullet.png' # пуля

# переменные счетчики
lost = 0
point = 0

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
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        bullet = Bullet(img_bullet,self.rect.centerx,self.rect.top,30,30,10)
        bullets.add(bullet)

# класс пули
class Bullet(GameSprite):
    # движение пули
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# класс спрайта-врага   
class Enemy(GameSprite):
    # движение врага
    def update(self):
        global lost
        self.rect.y += self.speed
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# создаем спрайты
ship = Player(img_hero, 5, win_height - 100, 100, 100, 10)

bullets = sprite.Group()

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 100, 100, randint(1, 5))
    monsters.add(monster)

# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
    # обработка нажатия кнопки пробел
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()

    if not finish:
        # обновляем фон
        window.blit(background,(0,0))

        # пишем текст на экране
        kill_point = font_for_score.render('Kills: '+str(point),1,(255,255,255))
        window.blit(kill_point,(10,10))

        lost_point = font_for_score.render('Lost: '+str(lost),1,(255,255,255))
        window.blit(lost_point,(10,50))

        # производим движения спрайтов
        ship.update()
        monsters.update()
        bullets.update()

        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        # Обработка столкновения пули с врагом
        if sprite.groupcollide(bullets,monsters,True,True):
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 100, 100, randint(1, 5))
            monsters.add(monster)
            point += 1

        if point == 5:
            window.blit(win_text,(100,200))
            finish = True

        if lost == 3 or sprite.spritecollide(ship,monsters,True):
            window.blit(lose_text,(100,200))
            finish = True

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
