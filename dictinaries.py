authors = {
    'Пушкин': 'Русский поэт, драматург и прозаик. Один из самых авторитетных литературных деятелей первой трети XIX века',
    'Толстой': 'Один из наиболее известных русских писателей и мыслителей, один из величайших писателей-романистов мира',
    'Бунин': 'Русский писатель, поэт и переводчик, лауреат Нобелевской премии по литературе 1933 года'}

surname = input('Фамилия автора:')
if surname in authors:
   print('Биография:', authors[surname])
else:
   otvet = input('Автор не найден. Добавить?')
   if otvet == 'да':
      bio = input('Его биография:')
      authors[surname] = bio
      print(authors)
   else:
      print('Ответ получен')

#Данные одного из читателей. Не менять!
student_card = {'номер': '324', 'фамилия': 'Иванов'}

print('Добро пожаловать!', student_card)

otvet = input('Личный кабинет: 1 - взять, 2 - вернуть, 3 - домой')
while otvet != '3':
    if otvet == '1':
        book = input('Введите название:')
        student_card['долг'] = book
    if otvet == '2':
        if 'долг' in student_card:
            del student_card['долг']

    print('Карточка читателя:',student_card)
    otvet = input('Ваше действие: 1 - взять, 2 - вернуть, 3 - домой')

print('Ждём вас:',student_card)