from random import shuffle, randint

print('Здравствуй хозяин, меня зовут ОЛЕГ')
request = input('Что желаете? ').lower()

while request not in 'пока':
    if 'привет' in request:
        print('Вечер в хату!')
    elif 'как дела' in request:
        print('Отлично, как у вас?')
    elif 'что делаешь' in request:
        print('Сижу')
    elif 'шутка' in request:
        jokes = ['Колобок повесился', 'Русалка села на шпагат', 'Рыба утонула']
        shuffle(jokes)
        print(jokes[0])
    elif 'фильмы' in request:
        genre = input('Введите интересующий вас жанр: ').lower()
        if genre in 'боевик':
            print('Атака титаника')
        elif genre in 'комедия':
            print('Один дома') 
        elif genre in 'ужас':
            print('Пила')
        else:
            print('Таких жанров я не знаю')
    elif 'игра' in request:
        print('Игра угадай число от 1 до 100')
        win_num = randint(1, 100) 
        for i in range(5):
            number = int(input('Введите число'))
            if number > win_num:
                print('Загаданное число меньше')
            elif number < win_num:
                print('Загаданное число больше')
            else:
                print('Поздравляем ты выйграл')
                break
    else:
        print('Извини, я тебя не понимаю')

    request = input('Что желаете? ').lower()

print('До скорых встреч!')
