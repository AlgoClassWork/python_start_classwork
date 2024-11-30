sales = input('Желаете изучить хиты продаж?')
if sales == 'да':
    category = input('Введите категорию:')
    if category == 'продукты':
        print('Молоко 1л, Печенье с изюмом, Персики')
    else:
        print('Стиральный порошок, Щётка для обуви')
else:
    print('Дайте знать, если передумаете!')


price1 = int(input('Цена первого товара')) 
price2 = int(input('Цена второго товара')) 
price3 = int(input('Цена третьего товара')) 

if price1 >= price2:
    if price1 >= price3:
        max_price = price1
    else:
        max_price = price3
else:
    if price2 >= price3:
        max_price = price2
    else:
        max_price = price3

print('Акция! К оплате за три товара:', max_price)
