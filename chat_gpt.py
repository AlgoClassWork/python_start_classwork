print('Здравствуйте господин я бот Виталя')
print('Я умею Шутить шутки рекомендовать Китайские мультфильмы')
print('Могу поиграть с вами и продать вам Хлам за дорого')

otvet = input('Что вы от меня хотите?').lower()
while otvet.find('пок') == -1:
    if otvet.find('прив') > -1:
        print('Вечер в хату')
    elif otvet.find('как') > -1:
        print('Отлично как у вас?')
    elif otvet.find('шутк') > -1:
        print('Колобок сел на шпагат')
    elif otvet.find('аним') > -1:
        genre = input('Какой жанр вас интересует?')
        if genre == 'боевик':
            print('Атака титаника')
        elif genre == 'романтика':
            print('Твоя апрельская ложь')
        elif genre == 'мистика':
            print('Dan dan')
        else:
            print('Извини такого жанра пока нет')


    otvet = input('Что вы от меня хотите?').lower()

