from random import randint

print('Здравствуйте мой господин меня зовут Антоха')
print('Я умею шутить шутки , Рекомендовать аниме')
print('Можем сыграть в игру, Купить акссесуары')

otvet = input('Чтобы вы от меня хотели?') 

while otvet != 'пока':

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

    elif otvet.find('фильм') != -1:
        genre = input('Какой жанр вам интересен?')
        if genre == 'комедия':
            print('Мальчишнк в вегасе')
        elif genre == 'детектив':
            print('Шерлок холмс')
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

    elif otvet.find('куп') != -1:
        print('Привествую вас в Антоха Шоп')
        print('У нас есть такие товары как:')
        print('Туалетка мумии 10$')
        print('Носки мамонта 50$')
        money = int(input('Сколько у вас деняк?'))
        tovar = input('Чтобы вы хотели купить?')
        while tovar != 'стоп' and money > 0:
            if tovar == 'туалетка' and money >= 10:
                money -= 10
                print('Вы купили туалетную бумагу мумии будьте осторожны она проклята')
                print('С вашего счета сняли 10$ у вас осталось', money,'$')
            elif tovar == 'носки' and money >= 50:
                money -= 50
                print('Вы купили носки мамонта будьте осторожны вас могли обмануть')
                print('С вашего счета сняли 50$ у вас осталось', money,'$')
            else:
                print('Такого товара у нас нет или у вас недостаточно деняк')

            tovar = input('Чтобы вы хотели купить?')
    else:
        print('Извини я не понимаю твой запрос')
        print('Я могу шутить играть рекомендовать аниме и продавать хлам')

    otvet = input('Чтобы вы от меня хотели?') 

print('До скорой встречи дядя!')
