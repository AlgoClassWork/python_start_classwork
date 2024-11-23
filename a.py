from pygame import *
#создаем экран
window = display.set_mode( (700,500) )
display.set_caption('Догонялки')
#загрузка игровых картинок
background = image.load('back.png')
background = transform.scale(background, (700,500))

pica = transform.scale(image.load('pica.png'), (100,100))
gita = transform.scale(image.load('gita.png'), (100,100))

pica_x, pica_y = 100, 100 #new
gita_x, gita_y = 400, 100 #new

#запускаем игровой цикл
game = True
while game:
    #отображение картинок
    window.blit(background, (0,0) )
    window.blit(pica, (pica_x,pica_y) ) #update
    window.blit(gita, (gita_x,gita_y) ) #update
    #обрабатываем нажатие на крестик
    for e in event.get():
        if e.type == QUIT:
            game = False

    press =  key.get_pressed()
    if press[K_w] and pica_y > 0:
        pica_y -= 3
    if press[K_s] and pica_y < 400:
        pica_y += 3
    if press[K_a] and pica_x > 0:
        pica_x -= 3
    if press[K_d] and pica_x < 600:
        pica_x += 3

    if gita_x > pica_x:
        gita_x -= 1
    if gita_x < pica_x:
        gita_x += 1
    if gita_y > pica_y:
        gita_y -= 1
    if gita_y < pica_y:
        gita_y += 1
    
    display.update()
