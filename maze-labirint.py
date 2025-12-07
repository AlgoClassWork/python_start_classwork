from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, cord_x, cord_y, width, height, speed):
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
        self.speed = speed
        self.width = width
        self.height = height

    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )
    
class Player(GameSprite):
    def move(self):
        keys = key.get_pressed() 
        if keys[K_d] and self.rect.x < 700 - self.width:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - self.height:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, cord_x, cord_y, width, height):
        self.width = width
        self.height = height
        self.image = Surface((width, height))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

# Создание окна
window = display.set_mode( size=(700, 500) )
display.set_caption('Лабиринт')
# Загрузка фона
back = transform.scale(image.load('back.jpg'), (700,500))
# Создание спрайтов
player = Player('player.png', 100, 100, 50, 50, 10)
enemy = GameSprite('enemy.png', 400, 100, 50, 50, 5)
wall1 = Wall(100, 200, 400, 20)
wall2 = Wall(100, 200, 20, 300)
wall3 = Wall(500, 100, 20, 300)

clock = time.Clock()
while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    window.blit(back, (0, 0))
    # Отображение спрайтов
    player.show()
    enemy.show()
    wall1.show()
    wall2.show()
    wall3.show()
    # Движение спрайтов
    player.move()
    
    if sprite.collide_rect(player, enemy):
        player.rect.x = 100
        player.rect.y = 100

    display.update()
    clock.tick(60)
