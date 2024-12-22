from pygame import *
# Основной игровой класс
class GameSprite(sprite.Sprite):
    def __init__(self, img, w, h, x, y):
        self.image = transform.scale( image.load(img), (w,h) )
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        x , y = mouse.get_pos()
        self.rect.centery = y

class Ai(GameSprite):
    def move(self):
        pass

class Ball(GameSprite):
    speed_x = 1
    speed_y = 1
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > 650 or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1

# Создаем игровые обьекты
player = Player('racket.png', 20, 100, 10, 200)
ai = GameSprite('racket.png', 20, 100, 670, 200)
ball = Ball('ball.png', 50, 50, 325, 225)
# Настройки экрана
window = display.set_mode((700,500))
display.set_caption('пинг-понг')
# Игровой цикл
game = True
while game:
    # Обработка нажатия на крестик
    for e in event.get():
        if e.type == QUIT:
            game = False
    # Отрисовка игровых обьектов
    window.fill((255,255,255))

    player.show()
    ai.show()
    ball.show()

    # Движение обьектов
    player.move()

    ball.move()

    display.update()
