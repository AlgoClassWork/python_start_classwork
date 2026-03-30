from random import shuffle, randint

print('👋 Здравствуйте, хозяин! Чем я могу вам сегодня помочь? 😎')
answer = input('👉 Чего желаете? ').lower()

while answer != 'off':
    if 'прив' in answer:
        print('😄 Еще раз приветствую, хозяин! Как вы поживаете?')
    
    elif 'как' in answer:
        print('🔥 Отлично! Работаю без багов (почти 😅)')
    
    elif 'что' in answer:
        print('🤖 Работаю для вас 24/7 без кофе ☕❌')
    
    elif 'шут' in answer:
        jokes = [
            '😂 Колобок повесился...',
            '🤣 Русалка села на шпагат...',
            '😅 Рыба утонула… бывает...',
            '🤡 Программист умер, но сделал откат системы',
            '😂 Почему Python не кусается? Потому что он не C++ 😎'
        ]
        shuffle(jokes)
        print(jokes[0])
    
    elif 'игра' in answer or 'угадай' in answer:
        print('🎯 Отлично! Я загадал число от 1 до 10 😏')
        number = randint(1, 10)
        tries = 0
        
        while True:
            guess = input('👉 Ваш вариант (или "выход"): ').lower()
            
            if guess == 'выход':
                print('😅 Сдаётесь? Ну ладно...')
                break
            
            if not guess.isdigit():
                print('⚠️ Введите число!')
                continue
            
            guess = int(guess)
            tries += 1
            
            if guess == number:
                print(f'🎉 Угадали! Это было число {number} 😎')
                print(f'📊 Попыток: {tries}')
                break
            elif guess < number:
                print('📉 Маловато! Попробуйте больше 😉')
            else:
                print('📈 Слишком много! Попробуйте меньше 😏')
    
    elif 'фильм' in answer:
        print('🎬 Ооо, кино! Люблю это дело 😎')
        genre = input('👉 Какой жанр вас интересует? ').lower()
        
        if 'боевик' in genre:
            action = ['💥 Железный человек', '🔫 Джон Уик', '🚗 Форсаж']
            shuffle(action)
            print('🎥 Советую:', action[0])
        
        elif 'комедия' in genre:
            comedy = ['😂 Час пик', '🤣 Мальчишник в Вегасе', '😆 Очень страшное кино']
            shuffle(comedy)
            print('🎥 Для настроения:', comedy[0])
        
        else:
            print('🤔 Я такого жанра не знаю...')
    
    else:
        print('😅 Извините, я вас не понимаю...')
    
    answer = input('👉 Чего желаете? ').lower()

print('👋 Буду ждать вас снова, хозяин! 😎')
