from pygame import *

#класс для добавления персонажей
class GameSprite(sprite.Sprite):
    def __init__(self,img,cord_x,cord_y,width,height):
        self.image = transform.scale(image.load(img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

#создание ракеты
player = GameSprite(img='sheep.png',cord_x=450,cord_y=500,width=100,height=100)

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
    
    #обработка нажантия на крестик
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    display.update()
