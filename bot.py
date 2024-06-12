from random import randint
print('Привет меня зовут Василий')
print('Вот что я умею:')
print('Рассказывать шутки, рекомендовать китайские мультики')
print('Могу поиграть с тобой и предложить купить вещи')
otvet = input('Что бы вы хотели?').lower()
while otvet.find('досвид') == -1:
    if otvet.find('шут') != -1: 
        print('Колобок повесился!!!')
    elif otvet.find('смотр') != -1:
        genre = input('Какой жанр вас интересует?')
        if genre == 'боевик':
            print('Начало, Темный рыцарь, Форсаж 111')
        elif genre == 'комедия':
            print('Мальчишник в вегасе, Тупой и еще тупее, Борат')
        else:
            print('Такого жанра у нас еще не добавили')
    elif otvet.find('игр') != -1:
        win_num = randint(1,100)
        for i in range(7):
            num = int(input('Введите число'))
            if num > win_num:
                print('Загаданое число меньше')
            elif num < win_num:
                print('Загаданое число больше')
            else:
                print('Вы выйграли пачку сухариков')
                break
            

    otvet = input('Что бы вы хотели?').lower()
