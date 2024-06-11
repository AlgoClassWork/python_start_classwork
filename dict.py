#Данные одного из читателей. Не менять!
student_card = {'номер': '324', 'фамилия': 'Иванов'}
print('Добро пожаловать!', student_card)
otvet = input('Личный кабинет: 1 - взять, 2 - вернуть, 3 - домой')
while otvet != '3':
    if otvet == '1':
        name = input('Введите название:')
        student_card['долг'] = name
        print('Карточка читателя:',student_card)
    if otvet == '2':
        if 'долг' in student_card:
            del student_card['долг']
        print('Карточка читателя:',student_card)
    otvet = input('Личный кабинет: 1 - взять, 2 - вернуть, 3 - домой')

print('Ждём вас:',student_card)



my_shelf = dict()
author = input('Введите автора (q - завершить):')
while author != 'q':
   books = list()
   book = input('Введите книгу (s - стоп):')
   while book != 's':
       books.append(book)
       book = input('Введите книгу (s - стоп):')
   my_shelf[author] = books
   author = input('Введите автора (q - завершить):')

for author in my_shelf:
   print(author, '-', my_shelf[author])

