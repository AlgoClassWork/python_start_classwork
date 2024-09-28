otdel  = {
    'Васильев' : {
        'должность': 'уборщик',
        'эффективность' : 100,
        'портфолио': ['dota2','csgo']
    },
    'Петров' : {
        'должность': 'сисадмин',
        'эффективность': 78,
        'портфолио': ['osu','minecraft']
    },
    'Байден' : {
        'должность': 'министр',
        'эффективность': 90,
        'портфолио': ['osu','minecraft']
    },
}

print('Фамилии всех сотрудников:',list(otdel.keys()))
sotrudnik = ''
max_effect = 0
for surname in otdel:
    if otdel[surname]['эффективность'] > max_effect:
        max_effect = otdel[surname]['эффективность']
        sotrudnik = surname
print('Самый эффективный',sotrudnik)
for surname in otdel:
    print('Должность',surname,'-',otdel[surname]['должность'])

