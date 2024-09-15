balance = int(input('Введите текущий баланс карты'))
while balance > 0 and input('Хотите сделать покупку (да/нет)?') == 'да':
    price = int(input('Введите цену'))
    if balance - price < 0:
        print('Недостаточно средств!')
    else:
        balance -= price
        print('Сумма', price, 'руб. списана со счёта.')
print('Доступная сумма:', balance, 'руб.')


start = int(input("Год начала сотрудничества с фондом"))
end = int(input("Год окончания сотрудничества с фондом"))
for year in range(start, end + 1):
    if year % 2 == 0:
        print(year, "год - серия конференций и круглых столов с экспертами.")
    else:
        print(year, "год - международный конкурс 'Стартап года'.")
