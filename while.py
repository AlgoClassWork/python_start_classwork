#Автоподсчёт суммы покупок
tovar = int(input('Стоимость товара (0 — покупок больше нет):'))
total = tovar
while tovar != 0:
    tovar = int(input('Стоимость товара (0 — покупок больше нет):')) 
    total = total + tovar
print('Стоимость всех покупок:', total)
