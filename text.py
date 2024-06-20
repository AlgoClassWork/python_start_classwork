otvet = input('Хотите добавить цитату? ')
while otvet != 'нет':
    file = open('quotes.txt', 'a', encoding='UTF8')
    quot = input('Напишите цитату: ')
    author = input('Введите автора: ')
    file.write(quot + '\n' + author + '\n')
    file.close()
    otvet = input('Хотите добавить цитату? ')
