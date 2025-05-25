from pygame import *  # Импорт всех модулей из pygame

class GameSprite(sprite.Sprite):
    """Базовый класс для всех спрайтов игры (игрок, враги, пули)"""

    def __init__(self, img, width, height, x, y, speed):
        super().__init__()
        # Загружаем и масштабируем изображение
        self.image = transform.scale(image.load(img), (width, height))
        # Получаем прямоугольник изображения для управления положением
        self.rect = self.image.get_rect()
        self.rect.x = x  # Устанавливаем начальную координату X
        self.rect.y = y  # Устанавливаем начальную координату Y
        self.speed = speed  # Устанавливаем скорость движения

    def show(self):
        """Метод отображения спрайта на экране"""
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite('block.png', 20, 100, 10, 200, 0)
computer = GameSprite('block.png', 20, 100, 670, 200, 3)
ball = GameSprite('ball.png', 50, 50, 350, 200, 5)
speed_x, speed_y = ball.speed, ball.speed

# Настройка окна игры
window = display.set_mode((700, 500))  # Установка размеров окна
display.set_caption('ПИНГ ПОНГ')  # Заголовок окна

# Игровой цикл
clock = time.Clock()  # Таймер для управления частотой кадров

while True:
    # Обработка событий
    for some_event in event.get():
        if some_event.type == QUIT:  # Выход из игры
            exit()

    # Заливка фона
    window.fill( (255,255,255) )

    # Отображение обьектов
    player.show()
    computer.show()
    ball.show()

    # Движение игрока
    mouse_x, mouse_y = mouse.get_pos()
    player.rect.centery = mouse_y

    # Движение мяча
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    # Движение компьютера
    if computer.rect.y < ball.rect.y:
        computer.rect.y += computer.speed
    else:
        computer.rect.y -= computer.speed

    # Проверка столкновений
    if ball.rect.x > 650 or ball.rect.x < 0:
        speed_x *= -1
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    # Обновление экрана
    display.update()
    clock.tick(100)  # Частота кадров — 100 FPS
