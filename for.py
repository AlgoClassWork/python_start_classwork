
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
