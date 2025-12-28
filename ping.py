from pygame import *

# подключение шрифтов
font.init()
font_count = font.Font(None, 80)

# игровые переменные
player_score = 0
ai_score = 0

# нам нужны такие картинки:
platform_img = "platform.png"  
ball_img = "ball.png"  

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, img, cord_x, cord_y, width, height):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(img), (width, height))
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
    # метод, отрисовывающий героя на окне
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Создаем окошко
display.set_caption("Пинг-понг")
window = display.set_mode((700, 500))

# создаем спрайты
player = GameSprite(platform_img, 10, 200, 20, 100)
ai = GameSprite(platform_img, 670, 200, 20, 100)
ball = GameSprite(ball_img, 330, 230, 50, 50)
speed_x, speed_y = 7, 7

# Основной цикл игры
clock = time.Clock()
while True:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            exit()

    # заливка фона цветом
    window.fill( (150, 250, 250) )
    # отображение спрайтов
    player.show()
    ai.show()
    ball.show()
    # отображение счета
    window.blit( font_count.render(f'{player_score}  |  {ai_score}', 1, (0,0,0)), (280, 10) )

    # управление игроком
    mouse_x, mouse_y = mouse.get_pos()
    if player.rect.centery > mouse_y:
        player.rect.y -= 5
    if player.rect.centery < mouse_y:
        player.rect.y += 5

    # управление игроком
    if ai.rect.centery > ball.rect.y:
        ai.rect.y -= 5
    if ai.rect.centery < ball.rect.y:
        ai.rect.y += 5

    # движение мяча
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if sprite.collide_rect(player, ball) or sprite.collide_rect(ai, ball):
        speed_x *= -1
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    # возврат мяча и подсчет баллов
    if ball.rect.x > 1200 or ball.rect.x < -500:
        if ball.rect.x > 1200:
            player_score += 1
        if ball.rect.x < -500:
            ai_score += 1

        ball.rect.x = 330
        ball.rect.y = 230
        speed_x *= -1

    display.update()
    clock.tick(60)
