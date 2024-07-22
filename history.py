from time import *

students = open('students.txt','r',encoding='utf-8')

total_iq = 0
people = 0

genius = []
stupid = []

start = time() 

for student in students:

    student_info = student.split() 
    student_name = student_info[0]
    student_surname = student_info[1]
    student_iq = int(student_info[2])

    total_iq += student_iq
    people += 1

    if student_iq > 160:
        genius.append(student_surname)
    if student_iq < 100:
        stupid.append(student_surname)

end = time() 

print('Средний iq балл исторической личности равен:', total_iq/people)
print('Список гениев на экране:', len(genius))
print('Список дурачков на экране:', len(stupid))
print('Анализ данных занял', end-start, 'с')
