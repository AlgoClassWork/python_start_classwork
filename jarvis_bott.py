from random import shuffle, randint

print('''
🤖 Приветствую, Хозяин!
Я — Джарвис, ваш цифровой напарник.
Могу:
• Поболтать 🤝
• Рассказать шутку 😂
• Сыграть в игру 🎲
• Порекомендовать фильм 🎬

(Для выхода напишите "выкл")
''')

# Фразы для ответов
greetings = ['Вечер в хату, командир! 😎', 'Хоп-хей, не стой у дверей! 🚪', 'Прив-прив! 0_0 🤖']
how_are_you = ['Круто! А у вас как? 🔥', 'Отлично, заряжен на 100%! ⚡', 'Поршиво... Шучу, я бот 😁']
jokes = [
    'Колобок повесился... 😐 Печально, но абсурдно.',
    'Русалка села на шпагат... теперь её зовут Морская звезда 🧜‍♀️✨',
    'Рыба утонула... Видимо, училась плавать у меня 🐟💀'
]

# Основной цикл
user_input = input('💬 Чем займёмся, мой создатель? ').lower()

while 'выкл' not in user_input:
    if 'прив' in user_input:
        shuffle(greetings)
        print(f'🤖 {greetings[0]}')

    elif 'дел' in user_input:
        shuffle(how_are_you)
        print(f'😄 {how_are_you[0]}')

    elif 'шут' in user_input:
        shuffle(jokes)
        print(f'😂 {jokes[0]}')

    elif 'игр' in user_input:
        secret_number = randint(1, 100)
        print('🎯 Я загадал число от 1 до 100. У тебя 5 попыток угадать!')

        for attempt in range(1, 6):
            num_input = input(f'Попытка {attempt}/5 — Введите число: ')

            if num_input.isdigit():
                guessed = int(num_input)

                if guessed > secret_number:
                    print('🔻 Ваше число больше загаданного.')
                elif guessed < secret_number:
                    print('🔺 Ваше число меньше загаданного.')
                else:
                    print('🎉 Поздравляю! Вы угадали число! Победа за вами 🏆')
                    break
            else:
                print('😅 Это не число. Вы теряете попытку...')

        else:
            print(f'😢 Увы, вы не угадали. Я загадал число {secret_number}.')

    elif 'филь' in user_input:
        print('🎬 Пока не умею советовать фильмы, но скоро научусь! Попробуйте позже 🍿')

    else:
        print('🤷‍♂️ Простите, я не понимаю такую команду. Попробуйте ещё раз.')

    user_input = input('\n💬 Что дальше, Хозяин? ').lower()

print('🛑 Выключаюсь... До скорых встреч, мой создатель! 🤖✌️')
