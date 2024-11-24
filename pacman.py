from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption('Лабиринт ужаса')

background = transform.scale(image.load('background3.png'), (win_width,win_height))

#музыка
#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0) )

    display.update()
    clock.tick(60)
