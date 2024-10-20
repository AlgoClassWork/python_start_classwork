file = open('poem.txt','r',encoding='utf-8')
text = file.read()
print(text)

answer = input('Хотите добавить еще одну цитату? ')
while answer != 'нет':
    citata = input('Введите цитату: ')
    author = input('Введите автора: ')
    file = open('poem.txt','a',encoding='utf-8')
    file.write('\n' + citata + '\n(' + author + ')\n')
    answer = input('Хотите добавить еще одну цитату?')


file = open('students.txt','r',encoding='utf-8')
students = file.readlines()
total_iq = 0
total_person = 0
for student in students:
    info = student.split()
    surname = info[0]
    name = info[1]
    iq = int(info[2])
    total_iq += iq
    total_person += 1

print('Средний IQ', total_iq/total_person)
    

Эйнштейн Альберт 160
Ньютон Исаак 180
Хокинг Стивен 160
Кюри Мари 150
Тесла Никола 160
Галилей Галилео 160
Франклин Бенджамин 160
Дарвин Чарльз 145
Толстой Лев 150
Достоевский Фёдор 150
Остин Джейн 135
Ганди Махатма 140
Черчилль Уинстон 150
Паркс Роза 140
Шанель Коко 140
Уайльд Оскар 140
Джобс Стив 160
Гейтс Билл 160
Цукерберг Марк 152
Маск Элон 155
Кеннеди Джон 150
Колумб Христофор 140
Пикассо Пабло 140
