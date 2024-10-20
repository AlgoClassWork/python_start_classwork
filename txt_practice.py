answer = input('Хотите добавить цитату: ') 
while answer != 'нет':
    quote = input('Введите цитату: ')
    author = input('Введите автора: ')
    file = open('quotes.txt','a',encoding='utf-8')
    file.write(author + ' : ' + quote + '\n')
    answer = input('Хотите добавить цитату: ') 
