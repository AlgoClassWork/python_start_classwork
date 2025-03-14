from pygame import *

# Общее описание персонажей
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    # способность отображаться на экране
    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

class Platform(GameSprite):
    def move(self):
        mouse_x, mouse_y = mouse.get_pos()
        self.rect.centerx = mouse_x

# Создание обьектов
platform = Platform(img='platform.png', x=300, y=450)
ball = GameSprite(img='ball.png', x=300, y=300)
speed_x, speed_y = 3, 3


enemys = sprite.Group()
count = 10
for i in range(3): 
    y = 10 + (70 * i) 
    x = 10 + (30 * i) 
    for i in range(count):
        enemy = GameSprite('enemy.png', x, y)
        enemys.add(enemy)
        x += 70
    count -= 1

# создание экрана
window = display.set_mode( (700,500) )
display.set_caption('Арканойд')
# игровой цикл
clock = time.Clock()
game = True
while game:
    # обработка крестика
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False
    # заливка фона
    window.fill( (200,200,250) )
    # отображение персонажей
    platform.show()
    ball.show()
    enemys.draw(window)
    #движение платформы
    platform.move()
    #движение мяча
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.x < 0 or ball.rect.x > 650:
        speed_x *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    #проверка столкновений
    if sprite.collide_rect(platform, ball) or sprite.spritecollide(ball, enemys, True):
        speed_y *= -1
    # обновление кадров
    display.update()
    # настройка частоты кадров
    clock.tick(120)
