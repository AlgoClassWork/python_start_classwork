from pygame import *
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
   direction = "left"
   def update(self):
       if self.rect.x <= 470:
           self.direction = "right"
       if self.rect.x >= win_width - 85:
           self.direction = "left"


       if self.direction == "left":
           self.rect.x -= self.speed
       else:
           self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height):
        self.image = Surface((wall_width, wall_height))
        self.image.fill((0,255,100))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


#Персонажи игры:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

wall_1 = Wall(10,10,650,10)
wall_2 = Wall(200,100,10,400)
wall_3 = Wall(200,400,400,10)


game = True
finish = False
clock = time.Clock()
FPS = 60


#музыка
#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

#надписи
font.init()
my_font = font.Font('Shrift.ttf',100)
text_win = my_font.render('ПОБЕДА',True,(0,255,0))
text_lose = my_font.render('ПРОИГРЫШ',True,(255,0,0))

while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       window.blit(background,(0, 0))
       player.update()
       monster.update()
      
       player.reset()
       monster.reset()
       final.reset()

       wall_1.reset()
       wall_2.reset()
       wall_3.reset()

       if sprite.collide_rect(player, final):
           window.blit(text_win,(200,200))
           finish = True

       if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3):
           window.blit(text_lose,(100,200))
           finish = True
           

   display.update()
   clock.tick(FPS)
