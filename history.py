from time import *

students = open('students.txt','r',encoding='utf-8')

total_iq = 0
people = 0

for student in students:
    student_info = student.split() 
    student_name = student_info[0]
    student_surname = student_info[1]
    student_iq = int(student_info[2])

    total_iq += student_iq
    people += 1

print('Средний iq балл исторической личности равен:', total_iq/people)




Александр Пушкин 120
Адольф Гитлер 99
Альберт Эйнштейн 160
Исаак Ньютон 160
Жан-Жак Руссо 145
Чарльз Дарвин 165
Фрэнсис Бэкон 170
Михаил Ломоносов 160
Александр Флеминг 130
Луи Пастер 145
Галилео Галилей 160
Уильям Шекспир 155
Карл Маркс 155
Наполеон Бонапарт 145
Лев Толстой 160
Фридрих Ницше 150
Стивен Хокинг 160
Герман Гессе 140
Рене Декарт 155
Михаил Кутузов 145
Леонардо да-Винчи 180
Никола Тесла 160
Жанн дАрк 120
Василий Жуковский 120
Леонард Бернштейн 125
Михаил Герцен 125
