balance = int(input('Введите текущий баланс карты'))
while balance > 0 and input('Хотите сделать покупку (да/нет)?') == 'да':
    price = int(input('Введите цену'))
    if balance - price < 0:
        print('Недостаточно средств!')
    else:
        balance -= price
        print('Сумма', price, 'руб. списана со счёта.')
print('Доступная сумма:', balance, 'руб.')
