marks = []
mark = int(input())
good_mark = 0
while mark != 0:
   marks.append(mark)
   if mark > 2:
      good_mark += 1
   mark = int(input())

print('Список оценок:',marks)
print('Успеваемость:',good_mark/len(marks) * 100)
