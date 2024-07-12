#Данные одного из читателей. Не менять!
student_card = {'номер': '324', 'фамилия': 'Иванов'}

print('Добро пожаловать!',student_card)
otvet = input('Личный кабинет: 1 - взять, 2 - вернуть, 3 - домой')
while otvet != '3':
    if otvet == '1':
        book = input('Введите название:')
        student_card['долг'] = book
        print('Карточка читателя:', student_card)
    if otvet == '2':
        if 'долг' in student_card:
            del student_card['долг']
        print('Карточка читателя:', student_card)

    otvet = input('Ваше действие: 1 - взять, 2 - вернуть, 3 - домой')
print('Ждём вас:',student_card)
