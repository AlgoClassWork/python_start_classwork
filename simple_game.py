#pip install pygame
from pygame import *

window = display.set_mode( (700, 500) )
back = image.load('back.png')
back = transform.scale( back, (700, 500) )

game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(back, (0, 0))
    display.update()
    
