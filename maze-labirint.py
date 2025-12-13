from pygame import *

# Класс спрайта
class GameSprite(sprite.Sprite):
    def __init__(self, img, cord_x, cord_y, width, height, speed):
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
        self.speed = speed
        self.width = width
        self.height = height

    # Отображение спрайта
    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

# Класс игрока 
class Player(GameSprite):
    # Движение игрока
    def move(self):
        keys = key.get_pressed() 
        if keys[K_d] and self.rect.x < 700 - self.width:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - self.height:
            self.rect.y += self.speed

# Класс врага 
class Enemy(GameSprite):
    # Движение врага (патрулирование)
    def move(self):
        if self.rect.x <= 300:
            self.side = 'право'
        if self.rect.x >= 700 - self.width:
            self.side = 'лево'

        if self.side == 'лево':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

# Класс стены
class Wall(sprite.Sprite):
    def __init__(self, cord_x, cord_y, width, height):
        self.width = width
        self.height = height
        self.image = Surface((width, height))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

    # Отображение стены
    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

# Создание окна
window = display.set_mode( size=(700, 500) )
display.set_caption('Лабиринт')
# Загрузка фона
back = transform.scale(image.load('back.jpg'), (700,500))
# Создание спрайтов
player = Player('player.png', 0, 450, 50, 50, 10)
enemy = Enemy('enemy.png', 650, 450, 50, 50, 5)
goal = GameSprite('goal.png', 440, 230, 50, 50, 0)

wall1 = Wall(100, 200, 400, 20)
wall2 = Wall(100, 200, 20, 300)
wall3 = Wall(500, 100, 20, 300)

walls = [wall1, wall2, wall3]

font.init()
my_font = font.Font(None, 150)
lose_text = my_font.render('YOU LOSE!', True, (255, 0, 0))
win_text = my_font.render('YOU WIN!', True, (0, 255, 0))

# Основной цикл игры
pause = False
clock = time.Clock()
while True:
    # Обработка событий
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()
        elif some_event.type == KEYDOWN:
            if some_event.key == K_r and pause:
                player.rect.x = 0
                player.rect.y = 450
                pause = False

    # Отрисовка фона
    window.blit(back, (0, 0))
    # Отображение спрайтов
    player.show()
    enemy.show()
    goal.show()
    for wall in walls:
        wall.show()
    # Движение спрайтов
    if not pause:
        player.move()
        enemy.move()

    # Проверка столкновений с врагом
    if sprite.collide_rect(player, enemy):
        window.blit(lose_text, (100, 200))
        pause = True

    # Проверка столкновений с целью
    if sprite.collide_rect(player, goal):
        window.blit(win_text, (100, 200))
        pause = True

    # Проверка столкновений с стенами
    for wall in walls:
        if sprite.collide_rect(player, wall):
            player.rect.x = 0
            player.rect.y = 450

    # Обновление экрана
    display.update()
    clock.tick(60)
