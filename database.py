database = {
    'Илон Маск' : {
        'должность': 'уборщик',
        'эффективность': 100,
        'портфолио': ['tesla','чистый унитаз']
    },
    'Джо Байден' : {
        'должность': 'спящий дед',
        'эффективность': 1,
        'портфолио': ['dota2','белый дом']
    },
    'Винни Пух' : {
        'должность': 'батя',
        'эффективность': 77,
        'портфолио': ['медовый завод','аренда шаров']
    },
}

otvet = input('Чтобы вы хотели узнать о наших сотрудниках?')
if otvet == 'фамилии':
    print('Фамилии наших сотрудников:')
    for surname in database:
        print('-',surname.split()[1])
if otvet == 'самый крутой':
    max_effectivnost = 0
    samyi_krutoi = ''

    for surname in database:
        if database[surname]['эффективность'] > max_effectivnost:
            max_effectivnost = database[surname]['эффективность']

    for surname in database:
        if database[surname]['эффективность'] == max_effectivnost:
            samyi_krutoi = surname

    print('Самая большая эффективность у', samyi_krutoi)
    
if otvet == 'должности':
    for surname in database:
        print(surname,' - ',database[surname]['должность'])
