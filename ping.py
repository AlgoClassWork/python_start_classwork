from pygame import *

# подключение шрифтов
font.init()
font_count = font.Font(None, 40)

# игровые переменные

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

# Основной цикл игры
clock = time.Clock()
while True:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            exit()

    # заливка фона цветом
    window.fill( (150, 250, 250) )

    display.update()
    clock.tick(60)
