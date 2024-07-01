from pygame import *

window = display.set_mode((700,500))

background = image.load('background.jpg')
background = transform.scale(background,(700,500))

pica = transform.scale(image.load('pica.png'),(100,100)) 
adolf = transform.scale(image.load('adolf.png'),(100,100)) 

pica_x, pica_y = 100, 200  #new
adolf_x, adolf_y = 500, 200 #new

end = 0

game = True 
while game:

    window.blit(background,(0,0))
    window.blit(adolf,(adolf_x,adolf_y))  
    window.blit(pica,(pica_x,pica_y)) 
    

    for game_event in event.get():
        if game_event.type == QUIT:
            game = False

    keys = key.get_pressed()
    if keys[K_w]:
        adolf_y -= 5
    if keys[K_s]:
        adolf_y += 5
    if keys[K_a]:
        adolf_x -= 5
    if keys[K_d]:
        adolf_x += 5

    if adolf_x < pica_x:
        pica_x -= 1
    else:
        pica_x += 1

    if adolf_y < pica_y:
        pica_y -= 1
    else:
        pica_y += 1

    end += 20
    if end > 5000:
        print('победа рейха')
        game = False

    time.delay(20)
    display.update()
