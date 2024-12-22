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
        mouse_x, mouse_y = mouse.get_pos()
        self.rect.centery = mouse_y

# Создаем игровые обьекты
player = Player('racket.png', 20, 100, 10, 200)
ai = GameSprite('racket.png', 20, 100, 670, 200)
ball = GameSprite('ball.png', 50, 50, 325, 225)
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

    player.show()
    ai.show()
    ball.show()

    # Движение игровых обьектов
    player.move()

    clock.tick(120)
    display.update()
