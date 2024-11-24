from pygame import *

# Игровая сцена
window = display.set_mode((700,500))
display.set_caption('Лабиринт ужаса')
back = transform.scale(image.load('background3.png'),(700,500))

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

    display.update()
    clock.tick(60)
    
