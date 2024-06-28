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

game = True
while game:

    window.fill((50,250,250))
    ball.update()
    raketka1.update()
    raketka2.update()
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
