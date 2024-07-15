trainings = {
    'Онбординг':{
        'ответственный':'Ершов В.С.',
        'темы': ['техника безопасности', 'работа в команде'],
        'дата': '15.05'
    },
    'Повышение квалификации':{
        'ответственный':'Мишин Н.В.',
        'темы': ['лидерство', 'компьютерная грамотность'],
        'дата': '20.11'
    },
}

print('Тренинги ProTeam')
print('1-названия тренингов, 2-инфо о тренинге')
otvet = input('Номер действия (off-выйти):')
while otvet != 'off':
    if otvet == '1':
        for training in trainings:
            print('-',training)
    if otvet == '2':
        name = input('Название тренинга:')
        if name in trainings:
            print(trainings[name]['ответственный'])
            print(trainings[name]['темы'])
            print(trainings[name]['дата'])
        else:
            print('Такого тренинга не существует!')
    otvet = input('Номер действия (off-выйти):')
        
