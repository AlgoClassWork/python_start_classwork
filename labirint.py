from pygame import *
#создание экрана
window = display.set_mode((1000,600))
display.set_caption('Лабиринт ужаса')
#загрузка изображений
back = transform.scale(image.load('back.jpg'),(1000,600))
#музыка
#mixer.init()
#mixer.music.load('music.mp3')
#mixer.music.play()
#игровой цикл
game = True
while game:
    #отображение картинок
    window.blit(back,(0,0))
    #обработка нажантия на крестик
    for some_event in event.get():
        if some_event.type == QUIT:
            game = False
    #обновление кадров
    display.update()
