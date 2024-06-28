from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,sprite_image,x,y):
        super().__init__()
        self.image = image.load(sprite_image)
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def update(self):
        window.blit(self.image,(self.hitbox.x,self.hitbox.y))

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

    ball.hitbox.x += speed_x
    ball.hitbox.y += speed_y

    if ball.hitbox.y > 450 or ball.hitbox.y < 0:
        speed_y *= -1

    if ball.hitbox.x > 650 or ball.hitbox.x < 0:
        speed_x *= -1

    #Управление ракеткой игрока
    mouse_x,mouse_y = mouse.get_pos()
    raketka1.hitbox.y = mouse_y
    #Управление ракеткой оппонента
    if ball.hitbox.y > raketka2.hitbox.y:
        raketka2.hitbox.y += 1
    else:
        raketka2.hitbox.y -= 1





    display.update()
