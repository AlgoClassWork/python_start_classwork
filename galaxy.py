from pygame import *
from random import *

#класс для добавления персонажей
class GameSprite(sprite.Sprite):
    def __init__(self,img,cord_x,cord_y,width,height,speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
        self.speed = speed

    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Rocket(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 900:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = randint(0,900)

#создание ракеты
player = Rocket(img='sheep.png',cord_x=450,cord_y=500,width=100,height=100,speed=5)

#создание группы врагов
enemys = sprite.Group()
for _ in range(10):
    enemy = Enemy('enemy.png',randint(0,900),0,100,100,randint(1,3))
    enemys.add(enemy)

#создание экрана
window = display.set_mode((1000,600))
display.set_caption('ШУТЕР')
#загрузка изображений
back = transform.scale(image.load('back.jpg'),(1000,600))

game = True
while game:
    #отображение фона
    window.blit(back,(0,0))
    #отображение корабля
    player.show()
    #движение персонажей
    player.move()
    #группа врагов
    enemys.draw(window)
    enemys.update()
    
    #обработка нажантия на крестик
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    display.update()
