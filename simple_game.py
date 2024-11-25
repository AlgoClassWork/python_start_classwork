from pygame import *

window = display.set_mode( (700,500) )
display.set_caption('Догонялки')

background = image.load('фон.jpg')
background = transform.scale(background, (700,500) )

game = True
while game:

    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(background, (0,0) )

    display.update()
