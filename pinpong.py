from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,sprite_image,x,y):
        super().__init__()
        self.image = image.load(sprite_image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

ball = GameSprite('tenis_ball.png',350,250)
raketka1 = GameSprite('racket.png',50,250)
raketka2 = GameSprite('racket.png',600,250)   

window = display.set_mode((700,500)) # Создаем экран указаного 

speed_x = 1
speed_y = 1

game = True
while game:

    window.fill((50,250,250))

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.update()
    raketka1.update()
    raketka2.update()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1

    #Управление ракеткой игрока
    mouse_x,mouse_y = mouse.get_pos()
    raketka1.rect.y = mouse_y
    #Управление ракеткой оппонента
    if ball.rect.y > raketka2.rect.y:
        raketka2.rect.y += 1
    else:
        raketka2.rect.y -= 1

    if sprite.collide_rect(raketka1,ball) or sprite.collide_rect(raketka2,ball):
        speed_x *= -1

    display.update()
