from pygame import *

# класс для создания персонажей
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, size_x, size_y):
        #загружаем картинку
        self.image = transform.scale(image.load(sprite_image), (size_x, size_y))
        # хитбокс
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
 
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# создание игровых персонажей
ball = GameSprite('ball.png',500,300,100,100)
player = GameSprite('player.png',0,300,100,150)
enemy = GameSprite('enemy.png',900,300,100,150)

# экран для игры
display.set_caption("поке-понг")
window = display.set_mode((1000,600))
background = transform.scale(image.load('fon.jpg'), (1000, 600))

# скорости мяча
ball_x = 5
ball_y = 5

# счет игроков
player_score = 0
enemy_score = 0

# шрифты
font.init()
game_font = font.Font('game_font.ttf',40)
the_end = game_font.render('THE END',1,(255,255,255))

# игровой таймер
fps = time.Clock()
# игровой цикл
game = True
while game:

    # обработка выхода
    for eve in event.get():
        if eve.type == QUIT:
            game = False

    # отображение фона
    window.blit(background,(0,0))
    # отображение персонажей
    ball.show()
    player.show()
    enemy.show()
    # передвижение мяча
    ball.rect.x += ball_x
    ball.rect.y += ball_y

    if ball.rect.y > 500 or ball.rect.y < 0:
        ball_y *= -1

    # движение игрока
    x , mouse_y = mouse.get_pos()
    player.rect.centery = mouse_y
    # движение врага
    if enemy.rect.y < ball.rect.y:
        enemy.rect.y += 3
    else:
        enemy.rect.y -= 3

    # отбивание мяча
    if sprite.collide_rect(ball,player) or sprite.collide_rect(ball,enemy):
        ball_x *= -1

    # обновление кадров
    fps.tick(60)
    display.update()
