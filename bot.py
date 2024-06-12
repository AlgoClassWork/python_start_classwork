from random import randint

print('Здравствуйте меня зовут бот Генадий')
print('Вот что я умею: шутить рекомендовать оняме')
print('Могу с тобой сыграть и продать тебе хлам')

otvet = input('Что бы вы от меня хотели?').lower()

while otvet.find('пока') == -1:
    if otvet.find('шутк') != -1:
        print('Заходит как то негр в бар и ...')
    elif otvet.find('аним') != -1:
        genre = input('Введите жанр:')
        if genre == 'приключение':
            print('НОРУТО')
        elif genre == 'экшен':
            print('Атака титаника')
        else:
            print('Таких жанров я не знаю')
    elif otvet.find('игр') != -1:
        win_num = randint(1,100)
        for i in range(7):
            num = int(input('Введите число:'))
            if num > win_num:
                print('Загаданое число меньше')
            elif num < win_num:
                print('Загаданое число больше')
            else:
                print('Вы выйграли пачку сухариков!')
                break
        if win_num != num:
            print('Азазазаза ты ...')
    elif otvet.find('куп') != -1:
        print('Добро пожаловать в Генадий шоп')
        print('у нас вы можете купить')
        print('слезы крокодила, мясо шимпанзе, голова пришельца')
        money = int(input('Сколько у вас деняк?'))
        tovar = input('Что вы хотите купить?')
        while money > 0 and tovar != 'выйти':
            if tovar == 'слезы':
                money -= 20
                print('Не плачьте у вас осталось',money,'$')
            elif tovar == 'мясо':
                money -= 5
                print('Очень сочное но у вас осталось', money , "$")
            else:
                print('Ну ты дядя даешь у нас такого нет!')
            tovar = input('Что нибудь еще?')
        print('Приятно было отнять ваши кровные')
    else:
        print('Я тебя не понимаю!')
    otvet = input('Что бы вы от меня хотели?').lower()

print('Ты кто такой? Давай досвидания!')
