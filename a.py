from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y):
        self.image =  transform.scale(image.load(img), (70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

hero = GameSprite('hero.png',200,200)
enemy = GameSprite('cyborg.png',400,200)

# Игровая сцена
window = display.set_mode((700,500))
display.set_caption('Лабиринт ужаса')
back = transform.scale(image.load('background.jpg'),(700,500))

# Музыка
#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

# Игровой таймер
clock = time.Clock()

# Игровой цикл
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(back, (0,0))

    hero.draw()
    enemy.draw()

    display.update()
    clock.tick(60)
    
