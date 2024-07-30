from pygame import *

window = display.set_mode((700,500))
background_image = image.load('background.png') 
background_image = transform.scale(background_image,(700,500)) 

pica =  transform.scale(image.load('pica.png'),(100,100)) 
adolf =  transform.scale(image.load('adolf.png'),(100,100)) 

adolf_x = 350 
adolf_y = 250 

pica_x = 0
pica_y = 0

fps = time.Clock()

game = True
while game:

    window.blit(background_image,(0,0))
    window.blit(pica,(pica_x,pica_y)) 
    window.blit(adolf,(adolf_x,adolf_y))  

    if pica_x > adolf_x:
        pica_x -= 1
    else:
        pica_x += 1

    if pica_y > adolf_y:
        pica_y -= 1
    else:
        pica_y += 1

    if pica_x == adolf_x and pica_y == adolf_y:
        game = False

    keys = key.get_pressed() 
    if keys[K_w] and adolf_y > 0:
        adolf_y -= 5
    if keys[K_s] and adolf_y < 400 :
        adolf_y += 5
    if keys[K_a] and adolf_x > 0:
        adolf_x -= 5
    if keys[K_d] and adolf_x < 600:
        adolf_x += 5
    

    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    fps.tick(60)
    display.update()
