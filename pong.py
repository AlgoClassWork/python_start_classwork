from pygame import *

# класс для создания персонажей
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, size_x, size_y, sprite_speed):
        #загружаем картинку
        self.image = transform.scale(image.load(sprite_image), (size_x, size_y))
        self.speed = sprite_speed
        # хитбокс
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
 
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# создание игровых персонажей
ball = GameSprite('ball.png',500,300,100,100,5)
player = GameSprite('player.png',0,300,100,150,5)
enemy = GameSprite('enemy.png',900,300,100,150,5)

# экран для игры
display.set_caption("поке-понг")
window = display.set_mode((1000,600))
background = transform.scale(image.load('fon.jpg'), (1000, 600))

# игровой таймер
fps = time.Clock()
# игровой цикл
game = True
while game:

    # обработка выхода
    for eve in event.get():
        if eve.type == QUIT:
            game = False

    # отображение фона
    window.blit(background,(0,0))
    # отображение персонажей
    ball.show()
    player.show()
    enemy.show()
    # обновление кадров
    fps.tick(60)
    display.update()
