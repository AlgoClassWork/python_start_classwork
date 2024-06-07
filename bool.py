price1 = int(input('Цена первого товара:'))
price2 = int(input('Цена второго товара:'))
price3 = int(input('Цена третьего товара:'))
max_price = 0
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
