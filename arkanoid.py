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

# Создание обьектов
platform = GameSprite(img='platform.png',x=300,y=450)
ball = GameSprite(img='ball.png', x=300, y=300)

enemys = sprite.Group()
x = 0
for i in range(10):
    enemy = GameSprite(img='enemy.png',x=x,y=0) 
    x += 70
    enemys.add(enemy)

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
    # обновление кадров
    display.update()
    # настройка частоты кадров
    clock.tick(120)
