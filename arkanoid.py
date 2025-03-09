from pygame import *

# Общее описание персонажей
class GameSprite:
    def __init__(self, img, x, y):
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    # способность отображаться на экране
    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

# Создание обьектов
platform = GameSprite(img='platform.png',x=300,y=450)
ball = GameSprite(img='ball.png', x=300, y=300)

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
    # обновление кадров
    display.update()
    # настройка частоты кадров
    clock.tick(120)
