from pygame import *

window = display.set_mode( (700,500) )
display.set_caption('Догонялки')

background = image.load('фон.png')
background = transform.scale(background, (700,500) )

pica = transform.scale(image.load('pica.png'), (100,100) )
gita = transform.scale(image.load('gita.png'), (100,100) )

pica_x, pica_y = 200, 200
gita_x, gita_y = 400, 200

clock = time.Clock()

game = True
while game:

    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(background, (0,0) )
    window.blit(pica, (pica_x, pica_y))
    window.blit(gita, (gita_x, gita_y))

    keys = key.get_pressed()

    if keys[K_w] and pica_y > 0:
        pica_y -= 3
    if keys[K_s] and pica_y < 400:
        pica_y += 3
    if keys[K_a] and pica_x > 0:
        pica_x -= 3
    if keys[K_d] and pica_x < 600:
        pica_x += 3
    
    clock.tick(60)
    display.update()
