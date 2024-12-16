from random import randint
from pygame import *

lost = 0

font.init()
count_font = font.Font(None,30)


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

# класс для врагов
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            lost += 1
            self.rect.y = 0
            self.rect.x = randint(0,600)

# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

# создаем спрайты
ship = Player('rocket.png', 5, win_height - 100, 80, 100, 10)

enemys = sprite.Group()

for i in range(5):
    enemy = Enemy('ufo.png',randint(0,600),0,100,50,randint(1,5))
    enemys.add(enemy)

# Основной цикл игры:
run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background, (0,0))

    lost_text = count_font.render(f'Пропущено: {lost}',1, (255,255,255))
    window.blit(lost_text, (10,10))

    ship.update()
    enemys.update()

    ship.show()
    enemys.draw(window)

    display.update()

    time.delay(30)
