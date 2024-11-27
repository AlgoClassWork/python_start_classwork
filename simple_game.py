from pygame import *

window = display.set_mode( (700,500) )
display.set_caption('Догонялки')

background = image.load('фон.png')
background = transform.scale(background, (700,500) )

pica = transform.scale(image.load('pica.png'), (100,100) )
gita = transform.scale(image.load('gita.png'), (100,100) )

game = True
while game:

    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    
    window.blit(background, (0,0) )
    window.blit(pica, (200,200))
    window.blit(gita, (400,200))

    display.update()
