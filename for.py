
for i in range(3):
    wish = input('Введите предпочтение:')
    print('Предпочтение учтено')
print('Система рекомендаций настроена!')



total = 0
count = int(input('Количество оценок:'))
for i in range(count):
    mark = int(input('Оценка:'))
    total += mark
print('Среднее:', total/count)


count = int(input('Число участников:'))
for i in range(count):
    name = input('Введите имя:')
    print('Добро пожаловать,',name)
print('Групповой чат создан!')



#проверка логина на содержание запрещенных символов
login = input('Введите логин:')
for symbol in login:
    if symbol in '=?*^$№@_':
        print('Запрещённый символ:', symbol)


for i in range(1,4):
    game = input('Введите название игры:')
    if game == 'FIFA':
        print('Поздравляем! Вы угадали с попытки №',i)
        break


number = input('Введите 1 - рекомендация, 2 - розыгрыш, off - завершить')
while number != 'off':
   if number == '1':
       preference = input('Введите предпочтение:')
       if preference == 'спорт':
           print('Подкаст Убойный спорт')
       else:
           print('Новый альбом Канье Уэста')
   elif number == '2':
       for i in range(1, 4):
           if input('Введите название группы') == 'Queen':
               print('Вы выиграли билет на концерт!')
               break
   number = input('Введите 1 - рекомендация, 2 - розыгрыш, off - завершить')


