from pygame import *

# Базовый класс
class GameSprite():
    def __init__(self, img, w, h, x, y):
        self.image = transform.scale(image.load(img), (w,h))
        self.x = x
        self.y = y

    def show(self):
        window.blit(self.image, (self.x,self.y)) 

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.x > 0:
            self.x -= 5
        if keys[K_d] and self.x < 630:
            self.x += 5

player = Player(img='rocket.png',w=70,h=100,x=300,y=400)
enemy = GameSprite(img='ufo.png',w=100,h=70,x=300,y=200)


# Создание и настройка экрана
window = display.set_mode((700,500))
display.set_caption('Шутер')
back = transform.scale(image.load('galaxy.jpg'), (700,500))

# Игровые переменные
game = True
# Игровой цикл
while game:
    # Обработка выхода из игры
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False
    # Отображение обьектов
    window.blit(back, (0,0))
    player.show()
    enemy.show()
    # Передвижение обьектов
    player.move()
   
    display.update()
