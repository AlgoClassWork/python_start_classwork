from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))

player = GameSprite('platform.png',10,200,10,100)
ai = GameSprite('platform.png',680,200,10,100)
ball = GameSprite('ball.png',325,225,50,50)

ball_x, ball_y = 5, 5 

clock = time.Clock()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill((255,255,255))
    # отображение персонажей
    player.show()
    ai.show()
    ball.show()
    # передвижение игрока
    player.rect.centery = mouse.get_pos()[1]
    # передвижение врага
    if ai.rect.centery > ball.rect.centery:
        ai.rect.y -= 4
    else:
        ai.rect.y += 4
    # передвижение мяча
    ball.rect.x += ball_x
    ball.rect.y += ball_y

    if ball.rect.y > 450 or ball.rect.y < 0:
        ball_y *= -1
    if ball.rect.x > 650 or ball.rect.x < 0:
        ball_x *= -1

    display.update()
    clock.tick(60)
