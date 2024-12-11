from pygame import *

window = display.set_mode( (700,500) )
display.set_caption('Космический шутер')

back = transform.scale(image.load('galaxy.jpg'), (700,500))

hero_img = transform.scale(image.load('rocket.png'), (70,100))
hero_x = 300
hero_y = 400

game = True
while game:
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False

    window.blit(back, (0,0))
    window.blit(hero_img, (hero_x, hero_y))

    display.update()
    

