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
