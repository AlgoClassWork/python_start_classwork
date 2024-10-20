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
