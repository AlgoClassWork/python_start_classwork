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

# Настройка окна игры
window = display.set_mode((700, 500))  # Установка размеров окна
display.set_caption('Шутер')  # Заголовок окна

# Игровой цикл
clock = time.Clock()  # Таймер для управления частотой кадров

while True:
    # Обработка событий
    for some_event in event.get():
        if some_event.type == QUIT:  # Выход из игры
            exit()

    # Заливка фона
    window.fill( (255,255,255) )

    # Обновление экрана
    display.update()
    clock.tick(100)  # Частота кадров — 100 FPS
