from random import randint

print('Здравствуйте человеки я сверх продвинутый ысскуственный ынтелек')
print('Я могу сделать для вас следущие действия')
print('Пошутить / Рекомендация китайских мультфильмов')
print('Поиграть / Продажа всякого хлама')

comand = input('Что бы вы от меня хотели?').lower()
while comand != 'прощай':
    if comand.find('шут') > -1:
        print('Колобок повесился')
    elif comand.find('аниме') > -1:
        genre = input('Введите интересующий вас жанр:')
        if genre == 'фантастика':
            print('Посмотрите В ином мире со смартфоном')
        elif genre == 'боевик':
            print('Посмотрите Атака титаника')
        else:
            print('Извини я таких жанров пока не знаю')
    elif comand.find('игр') > -1:
        win_num = randint(1,100) 
        for i in range(7):
            num = int(input('Введите число'))
            if num > win_num:
                print('Загаданное число меньше')
            elif num < win_num:
                print('Загаданное число больше')
            else:
                print('Вы выйграли пачку сухариков!')
                break
    else:
        print('Извини бро я тебя не понимаю ;(')

    comand = input('Что то еще?').lower()

print('Буду ждать тебя господин')
