from random import randint

print('Здравствуйте мой господин меня зовут Антоха')
print('Я умею шутить шутки , Рекомендовать аниме')
print('Можем сыграть в игру, Купить акссесуары')

otvet = input('Чтобы вы от меня хотели?') 

while otvet != 'стоп':
    
    if otvet.find('шут') != -1:
        print('Колобок повесился')

    elif otvet.find('аним') != -1:
        genre = input('Какой жанр вам интересен?')
        if genre == 'фантастика':
            print('Гарри Поттер')
        elif genre == 'боевик':
            print('Атака Титаника')
        else:
            print('Такого жанра у нас нет')

    elif otvet.find('игр') != -1:
        win_num = randint(0,100) 
        for popytka in range(10):
            num = int(input('Введите число'))
            if num < win_num:
                print('Ваше число меньше загаданого')
            elif num > win_num:
                print('Ваше число больше загаданого')
            else:
                print('Поздравляем вы выйграли пачку сухариков')
                break

    otvet = input('Чтобы вы от меня хотели?') 
