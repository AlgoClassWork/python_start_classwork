from random import shuffle, randint

print('''
Здравствуйте, Хозяин
Меня зовут Джарвис и я умею
Общаться, шутить, рекомендовать фильмы
Могу сыграть с вами в игру
''')

greetings = ['Вечер в хату', 'Хоп хей', 'Приффетик 0_0']
dela = ['Круто как сам?', 'Отлично как у вас', 'Поршиво я бот']
jokes = ['колобок повесился', 'русалка села на шпагат', 'рыба утонула']

answer = input('Что бы вы хотели?').lower()
while 'выкл' not in answer:
    if 'прив' in answer:
        shuffle(greetings)
        print(greetings[0])
    elif 'дел' in answer:
        shuffle(dela)
        print(dela[0])
    elif 'шут' in answer:
        shuffle(jokes)
        print( jokes[0] )
    elif 'игр' in answer:
        win_num = randint(1,100)
        print('Я загадал число от 1 до 100 попробуй угадать')
        for i in range(5):
            num = int(input('Введите число:'))
            if num > win_num:
                print('Ваше число больше загадонного')
            elif num < win_num:
                print('Ваше число меньше загаданоого')
            else:
                print('Поздравляем вы победили')
                break

    elif 'филь' in answer:
        # Логика для рекомендаций фильмов
        pass
    else:
        print('Я не понимаю такой команды')
    answer = input('Что бы вы хотели?').lower()
