from pygame import *

class GameSprite():
    def __init__(self, img, x, y):
        self.image = transform.scale(image.load(img),(70,70))
        self.x = x
        self.y = y

    def show(self):
        window.blit(self.image,(self.x,self.y))

hero = GameSprite(img='hero.png', x=200, y=200)
enemy = GameSprite(img='cyborg.png', x=400, y=200)

window = display.set_mode( (700,500) )
display.set_caption('Лабиринт')

background = transform.scale(image.load('background.jpg'), (700,500))

#музыка
#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

clock = time.Clock()
game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    hero.show()
    enemy.show()

    display.update()
    clock.tick(60)
