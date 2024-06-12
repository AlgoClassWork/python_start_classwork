database = {
    'Гейб Ньюэл': {
        'должность': 'директор',
        'эффективность': 10,
        'проекты': ['dota 2','cs-go 2','half-life 2']
    },
    'Илон Маск': {
        'должность': 'гений',
        'эффективность': 30,
        'проекты': ['tesla','space-x','pay-pal']
    },
    'Павел Вольнадуров': {
        'должность': 'телеграмм шутник',
        'эффективность': 30,
        'проекты': ['telegram','comedy-club','V-Odnoklassnikah']
    },
}

question = input('Что бы хотели узнать о наших сотрудниках?')
while question != 'off':
    if question == 'фамилии':
        print('Фамилии сотрудников:')
        for surname in database:
            print('-',surname.split()[1])
    elif question == 'эффективность':
        effectivnost = []
        for surname in database:
            effectivnost.append(database[surname]['эффективность'])
        effectivnost.sort()
        max_effect = effectivnost[-1]
        samyi_krutoi = ''
        for surname in database:
            if database[surname]['эффективность'] == max_effect:
                samyi_krutoi = surname
        print('Самый эффективный сотрудник:', samyi_krutoi)
    elif question == 'должности':
        print('Должности наших сотрудников:')
        for surname in database:
            print(surname.split()[0],'-',database[surname]['должность'])

    question = input('Что бы хотели узнать о наших сотрудниках?')
    
