#Автоподсчёт суммы покупок
tovar = int(input('Стоимость товара (0 — покупок больше нет):'))
total = tovar
while tovar != 0:
    tovar = int(input('Стоимость товара (0 — покупок больше нет):')) 
    total = total + tovar
print('Стоимость всех покупок:', total)


#Подсчёт категорий товаров
category = input('Категория (end - завершить):')
count = 0
while category != 'end':
    count += 1
    category = input('Категория (end - завершить):')

print('Всего категорий товаров:', count)
