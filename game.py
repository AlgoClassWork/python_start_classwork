from pygame import *

window = display.set_mode( (700,500) )
background = image.load('fon.png')

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit( background, (0,0) )
    display.update()
