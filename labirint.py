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


class Wall(sprite.Sprite):
    def __init__(self,cord_x,cord_y,width,height):
        self.image = Surface((width,height))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

#создание стен
wall_1 = Wall(cord_x=200,cord_y=200,width=20,height=500)
wall_2 = Wall(cord_x=400,cord_y=200,width=600,height=20)
wall_3 = Wall(cord_x=200,cord_y=400,width=400,height=20)

    
#создание игровых обьектов
player = GameSprite(img='hero.png',cord_x=0,cord_y=450,width=150,height=150)
enemy = GameSprite(img='enemy.png',cord_x=800,cord_y=200,width=100,height=150)
goal = GameSprite(img='goal.png',cord_x=850,cord_y=500,width=150,height=100)
#создание экрана
window = display.set_mode((1000,600))
display.set_caption('Лабиринт ужаса')
#загрузка изображений
back = transform.scale(image.load('back.jpg'),(1000,600))
#музыка
#mixer.init()
#mixer.music.load('music.mp3')
#mixer.music.play()
#надписи
font.init()
shrift = font.Font('myfont.ttf',150)
win_label = shrift.render('YOU WIN',True,(0,255,0))
lose_label = shrift.render('YOU LOSE',True,(255,0,0))
#игровой цикл
timer = time.Clock()
game = True
finish = False
while game:
    #отображение картинок
    window.blit(back,(0,0))
    player.show()
    enemy.show()
    goal.show()

    wall_1.show()
    wall_2.show()
    wall_3.show()

    if not finish:

        #движение персонажей
        keys = key.get_pressed()
        if keys[K_w] and player.rect.y > 0:
            player.rect.y -= 5
        if keys[K_s] and player.rect.y < 450:
            player.rect.y += 5
        if keys[K_a] and player.rect.x > 0:
            player.rect.x -= 5
        if keys[K_d] and player.rect.x < 850:
            player.rect.x += 5

        if player.rect.x < enemy.rect.x:
            enemy.rect.x -= 1
        else:
            enemy.rect.x += 1

        if player.rect.y < enemy.rect.y:
            enemy.rect.y -= 1
        else:
            enemy.rect.y += 1

    #проверка столкновений
    if sprite.collide_rect(player,wall_1) or sprite.collide_rect(player,wall_2) or sprite.collide_rect(player,wall_3):
        window.blit(lose_label,(100,250))
        finish = True

    if sprite.collide_rect(player,enemy):
        window.blit(lose_label,(100,250))
        finish = True
        
    if sprite.collide_rect(player,goal):
        window.blit(win_label,(100,250))
        finish = True


    #обработка нажантия на крестик
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    #обновление кадров
    timer.tick(100)
    display.update()
