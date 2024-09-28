test_results = [
    [85.4, 71.6, 93.2, 65.8, 45.0],
    [89.5, 80.0, 95.5, 76.5, 72.0]
]

average = 0
for result in test_results[0]:
    average += result
print('Средний результат «до»:', average/len(test_results[0]))

average = 0
for result in test_results[1]:
    average += result
print('Средний результат «после»:', average/len(test_results[1]))




departments = {
    'продажи':{
        'сотрудники': ['Гришин', 'Иванова'],
        'менеджер': 'Иванова',
        'заведующий': 'Гришин'
    },
    'разработка':{
        'сотрудники': ['Васильев', 'Ежова', 'Петрова'],
        'менеджер': 'Ежова',
        'заведующий': 'Петрова'
    }
}

#допиши вывод данных
print('Заведующие отделов:')
for department in departments:
    print('-',departments[department]['заведующий'])
print('Проектные менеджеры отделов:')
for department in departments:
    print('-',departments[department]['менеджер'])



trainings = {
    'Онбординг': {
        'ответственный': 'Ершов В.С.',
        'темы': ['техника безопасности', 'работа в команде'],
        'дата': '15.05'
    },
    'Повышение квалификации': {
        'ответственный': 'Мишин Н.В.',
        'темы': ['лидерство', 'компьютерная грамотность'],
        'дата': '20.11'
    }
}

print('Тренинги ProTeam')
print('1-названия тренингов, 2-инфо о тренинге')
otvet = input('Номер действия (off-выйти):')
while otvet != 'off':
    if otvet == '1':
        for training in trainings:
            print('-',training)
    if otvet == '2':
        training = input('Название тренинга:')
        if training in trainings:
            print(trainings[training]['ответственный'])
            print(trainings[training]['темы'])
            print(trainings[training]['дата'])
        else:
            print('Такого тренинга не существует!')

    otvet = input('Номер действия (off-выйти):')
        
