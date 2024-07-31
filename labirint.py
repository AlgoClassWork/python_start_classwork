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
    
player = GameSprite(img='hero.png',cord_x=0,cord_y=450,width=150,height=150)
enemy = GameSprite(img='enemy.png',cord_x=800,cord_y=200,width=100,height=150)
goal = GameSprite(img='goal.png',cord_x=850,cord_y=500,width=150,height=100)
#создание экрана
window = display.set_mode((1000,600))
display.set_caption('Лабиринт ужаса')
#загрузка изображений
back = transform.scale(image.load('back.jpg'),(1000,600))
#музыка
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
#игровой цикл
game = True
while game:
    #отображение картинок
    window.blit(back,(0,0))
    player.show()
    enemy.show()
    goal.show()
    #обработка нажантия на крестик
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    #обновление кадров
    display.update()
