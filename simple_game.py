from pygame import *

window = display.set_mode((700,500))

back_image = image.load('back.png') 
back_image = transform.scale(back_image,(700,500)) 

pica = image.load('pica.png') 
pica = transform.scale(pica,(100,100))  

pica_x = 0 #new
pica_y = 0 #new

game = True
while game:

    window.blit(back_image,(0,0)) 
    window.blit(pica,(pica_x,pica_y))  #update

    keys = key.get_pressed() # new
    if keys[K_w]:
        pica_y -= 1
    if keys[K_s]:
        pica_y += 1
    if keys[K_a]:
        pica_x -= 1
    if keys[K_d]:
        pica_x += 1
    
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    display.update() 