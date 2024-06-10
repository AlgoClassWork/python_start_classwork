#Автоподсчёт суммы покупок
tovar = int(input('Стоимость товара (0 — покупок больше нет):')) 
total = tovar 
while tovar != 0:
    tovar = int(input('Стоимость товара (0 — покупок больше нет):')) 
    total = total + tovar

print('Стоимость всех покупок:', total)



#автомат для выдачи талонов
talon = input('Введите 0 — получить талон, 1 — выключить аппарат:')
count = 1
while talon != '1':
    if talon == '0':
        print('талон номер',count)
        count += 1
        
    talon = input('Введите 0 — получить талон, 1 — выключить аппарат:')
