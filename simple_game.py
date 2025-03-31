from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

platform = GameSprite('platform.png', 300, 450)
ball = GameSprite('ball.png', 350, 250)
speed_x, speed_y = 5, 5

enemys = sprite.Group()

def create_enemys():
    count = 9
    for i in range(3): 
        x = 20 + (35 * i)
        y = 20 + (60 * i)
        for i in range(count):
            enemy = GameSprite('enemy.png', x, y)
            enemys.add(enemy)
            x += 75
        count -= 1

create_enemys()

window = display.set_mode( (700,500) )
display.set_caption('Арканойд')

# работа со шрифтами
font.init()
my_font = font.Font(None, 150)
my_font2 = font.Font(None, 50)
lose_text = my_font.render('YOU LOSE',1,(255,0,0))
restart_text = my_font2.render('PRESS R TO RESTART GAME',1,(255,255,255))

clock = time.Clock()

game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False
        elif some_event.type == KEYDOWN and some_event.key == K_r:
            ball.rect.x, ball.rect.y = 250, 350
            create_enemys()
    # Отображение фона и персонажей
    window.fill( (200,200,255) )
    platform.show()
    ball.show()
    enemys.draw(window)
    # Движение платформы
    mouse_x, mouse_y = mouse.get_pos() 
    platform.rect.centerx = mouse_x
    # Движение мяча
    ball.rect.x += speed_x 
    ball.rect.y += speed_y
    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    # Проверка столкновений
    if sprite.collide_rect(ball, platform):
        speed_y *= -1
    if sprite.spritecollide(ball, enemys, True):
        speed_y *= -1
    # Условия победы и поражения
    if ball.rect.y > 500:
        window.blit(lose_text, (100,200))
        window.blit(restart_text, (130,300))
        
    display.update()
    clock.tick(60)
