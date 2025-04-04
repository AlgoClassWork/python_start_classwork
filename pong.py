from pygame import *
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
        x , y = mouse.get_pos()
        self.rect.centery = y

class Ai(GameSprite):
    def move(self, ball):
        if self.rect.centery > ball.rect.centery:
            self.rect.y -= 3
        else:
            self.rect.y += 3

class Ball(GameSprite):
    speed_x = 4
    speed_y = 4
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1

    def collide(self, player, ai):
        if sprite.collide_rect(self, player) or sprite.collide_rect(self, ai):
            self.speed_x *= -1

    def outside(self):
        global player_score, ai_score
        if self.rect.x > 650:
            player_score += 1
            self.rect.x = 325
            self.rect.y = 225
            time.delay(1000)
        if self.rect.x < 0:
            ai_score += 1
            self.rect.x = 325
            self.rect.y = 225
            time.delay(1000)


# Создаем игровые обьекты
player = Player('racket.png', 20, 100, 10, 200)
ai = Ai('racket.png', 20, 100, 670, 200)
ball = Ball('ball.png', 50, 50, 325, 225)
# Настройки экрана
window = display.set_mode((700,500))
display.set_caption('пинг-понг')
# Надписи
font.init()
score_font = font.Font(None, 40)
# Игровые переменные
player_score = 0
ai_score = 0
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
    
    window.blit(score_font.render(f'Очки: {player_score}',1,(0,0,0)), (10,10))
    window.blit(score_font.render(f'Очки: {ai_score}',1,(0,0,0)), (580,10))

    player.show()
    ai.show()
    ball.show()

    # Движение обьектов
    player.move()
    ai.move(ball)
    ball.move()

    ball.collide(player, ai)
    ball.outside()

    display.update()
    clock.tick(100)
