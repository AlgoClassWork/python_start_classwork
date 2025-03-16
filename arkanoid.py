from pygame import *

# Общее описание персонажей
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    # способность отображаться на экране
    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

class Platform(GameSprite):
    def move(self):
        mouse_x, mouse_y = mouse.get_pos()
        self.rect.centerx = mouse_x

# Создание обьектов
platform = Platform(img='platform.png', x=300, y=450)
ball = GameSprite(img='ball.png', x=300, y=300)
speed_x, speed_y = 3, 3

def create_enemys():
    count = 7
    for i in range(3): 
        y = 10 + (70 * i) 
        x = 20 + (50 * i) 
        for i in range(count):
            enemy = GameSprite('enemy.png', x, y)
            enemys.add(enemy)
            x += 100
        count -= 1
        
enemys = sprite.Group()
create_enemys()
# создание экрана
window = display.set_mode( (700,500) )
display.set_caption('Арканойд')

# оформление
font.init()
my_font = font.Font(None, 150) 
my_font2 = font.Font(None, 50) 
lose = my_font.render('YOU LOSE', 1, (255,0,0))
win = my_font.render('YOU WIN!', 1, (0,255,0))
reset_game = my_font2.render('PRESS R TO RESET GAME', 1, (0,0,255))
# подсчет врагов
total = 0
# игровой цикл
clock = time.Clock()
finish = False
game = True
while game:
    # обработка крестика
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False
        elif some_event.type == KEYDOWN:
            if some_event.key == K_r:
                ball.rect.y = 200
                total = 0
                finish = False
                create_enemys()

    if not finish:
        # заливка фона
        window.fill( (200,200,250) )
        # отображение персонажей
        platform.show()
        ball.show()
        enemys.draw(window)
        #движение платформы
        platform.move()
        #движение мяча
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.x < 0 or ball.rect.x > 650:
            speed_x *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        #проверка столкновений
        if sprite.collide_rect(platform, ball):
            speed_y *= -1
        if sprite.spritecollide(ball, enemys, True):
            speed_y *= -1
            total += 1
        # проигрыш
        if ball.rect.y > 500:
            window.blit(lose, (100,200))
            window.blit(reset_game, (150,300))
            finish = True
        if total == 1:
            window.blit(win, (100,200))
            window.blit(reset_game, (150,300))
            finish = True
        # обновление кадров
        display.update()
        # настройка частоты кадров
        clock.tick(120)

    
