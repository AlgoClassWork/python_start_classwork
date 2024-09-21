subjects = list()
subject = input('Введите предмет').lower()
while subject != '0':
    if subject in subjects:
        print('Этот предмет уже записан')
    else:
        subjects.append(subject)
    subject = input('Введите предмет').lower()

subjects.sort()
print('Список предметов:',subjects)
    

marks = []
mark = int(input('Введите оценку'))
total = 0
while mark != 0:
   marks.append(mark)
   if mark > 2:
      total += 1
   mark = int(input('Введите оценку'))

print('Список оценок:',marks)
print('Успеваемость:',total/len(marks) * 100)
