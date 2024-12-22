from pygame import *
# Игровые переменные
pl_point = 0
ai_point = 0
# Работа с шрифтом
font.init()
my_font = font.Font(None, 40)
# Основной игровой класс
class GameSprite(sprite.Sprite):
    def __init__(self, img, w, h, x, y):
        self.image = transform.scale( image.load(img), (w,h) )
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        mouse_x, mouse_y = mouse.get_pos()
        self.rect.centery = mouse_y

class Ball(GameSprite):
    speed_x = 5
    speed_y = 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def collide_platform(self):
        if sprite.collide_rect(self, player) or sprite.collide_rect(self, ai):
            self.speed_x *= -1

    def collide_wall(self):
        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1

    def respawn(self):
        if self.rect.x > 650 or self.rect.x < 0:
            self.rect.x = 325
            self.rect.y = 225
            time.delay(1000)

class Ai(GameSprite):
    def move(self):
        if self.rect.centery < ball.rect.centery:
            self.rect.y += 4
        else:
            self.rect.y -= 4
        
# Создаем игровые обьекты
player = Player('racket.png', 20, 100, 10, 200)
ai = Ai('racket.png', 20, 100, 670, 200)
ball = Ball('ball.png', 50, 50, 325, 225)
# Настройки экрана
window = display.set_mode((700,500))
display.set_caption('пинг-понг')
# Игровой цикл
clock = time.Clock()
game = True
while game:
    # Обработка нажатия на крестик
    for e in event.get():
        if e.type == QUIT:
            game = False
    # Отрисовка игровых обьектов
    window.fill((255,255,255))
    
    window.blit(my_font.render(f'Очки: {pl_point}', 1, (0,0,0)), (10,10))
    window.blit(my_font.render(f'Очки: {ai_point}', 1, (0,0,0)), (580,10))

    player.show()
    ai.show()
    ball.show()

    # Движение игровых обьектов
    player.move()
    ball.move()
    ai.move()

    ball.collide_platform()
    ball.collide_wall()
    ball.respawn()

    clock.tick(100)
    display.update()
