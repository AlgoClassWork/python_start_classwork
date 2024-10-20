answer = input('Хотите добавить цитату: ') 
while answer != 'нет':
    quote = input('Введите цитату: ')
    author = input('Введите автора: ')
    file = open('quotes.txt','a',encoding='utf-8')
    file.write(author + ' : ' + quote + '\n')
    answer = input('Хотите добавить цитату: ') 


Наруто Узумаки 120 166
Леви Аккерман 160 160
Гарри Поттер 125 170
Тони Старк 180 174
Кларк Кент 180 191
Эдвард Элрик 150 165
Дарт Вейдер 140 202
Люпен Третий 135 178
Саске Учиха 130 168
Джон Сноу 140 180
Питер Паркер 145 178
Микки Маус 100 70


file = open('person.txt','r',encoding='utf-8')
heroes = file.readlines()
amount_hero = len(heroes)
total_height = 0
for hero in heroes: 
    hero = hero.split()  
    name = hero[0]
    surname = hero[1]
    iq = int(hero[2])
    height = int(hero[3])
    total_height += height

print('Средний рост персонажа',total_height/amount_hero)
