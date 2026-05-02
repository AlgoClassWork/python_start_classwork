from random import choice, randint

print("🤖 Бот запущен! Напишите что-нибудь...")

while True:
    answer = input('📝 Вы: ').lower()

    if 'прив' in answer or 'здрав' in answer:
        print(choice([
            '👋 Здравствуйте, хозяин!',
            '😄 Привет! Рад вас видеть!',
            '🤖 Приветствую! Чем займёмся сегодня?'
        ]))

    elif 'шут' in answer:
        print(choice([
            '😂 Программист — это машина для кофе ☕➡️💻',
            '🤣 31 OCT = 25 DEC (поймут не все)',
            '😅 Я бы рассказал шутку про баг... но она не работает'
        ]))

    elif 'игра' in answer or 'угадай' in answer:
        print('🎮 Игра "Угадай число" началась!')
        secret = randint(1, 100)
        attempts = 0

        while True:
            guess = input('🔢 Введите число от 1 до 100 (или "выход"): ').lower()

            if guess == 'выход':
                print(f'🚪 Вы вышли из игры. Загаданное число было: {secret}')
                break

            if not guess.isdigit():
                print('⚠️ Введите именно число!')
                continue

            guess = int(guess)
            attempts += 1

            if guess < secret:
                print('📉 Слишком маленькое число!')
            elif guess > secret:
                print('📈 Слишком большое число!')
            else:
                print(f'🎉 Поздравляю! Вы угадали число {secret} за {attempts} попыток!')
                break

    elif 'пока' in answer:
        print('👋 До встречи!')
        break

    else:
        print('🤔 Я вас не понимаю...')
