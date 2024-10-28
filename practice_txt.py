otvet = input('Хотите добавить цитату? ')
while otvet != 'нет':
    quote = input('Введите цитату: ')
    author = input('Введите автора: ')
    file = open('quote.txt','a',encoding='utf-8')
    file.write('\n' + quote + '\n' + author + '\n')
    otvet = input('Хотите добавить цитату? ')

print('Ваш цитатник:')
file = open('quote.txt','r',encoding='utf-8')
print( file.read() )


Наруто 167
Гарри-Поттер 150
Бен-Тен 140
Супермен 185
Спайдермен 175
Бэтмен 182
Халк 240
Лея-Органа 160
Дарт-Вейдер 180
Лиона 155
Чудо-Женщина 175
Железный-Человек 180
Гринч 170
Пикачу 40
Гомера 175
Марио 155
Соник 90
Кот-Генерал 160
Мистер-Робот 180
Дедпул 185



from time import time
heroes = open('hero.txt','r',encoding='utf-8')
total_height = 0
amount_hero = 0
max_height = 0 #new
highest_person = '' #new
start = time() 
for hero in heroes:
    name = hero.split()[0] 
    height = int(hero.split()[1]) 
    total_height += height
    amount_hero += 1
    if height > max_height: #new
        max_height = height 
        highest_person = name #new
end = time() 
print('Средний рост 20 персонажей',total_height/amount_hero,'см') 
print('Самый высокий персонаж', highest_person)   #new
print('Прошло',end-start,'с')
