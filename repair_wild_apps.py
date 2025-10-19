import pandas
# Извлечение данных
wild_apps = pandas.read_csv('wild_apps.csv')

# Чиним наши данные
# Заменяем пустоту в колонке рейтинг на 0
average_rating = wild_apps['Rating'].mean()
wild_apps['Rating'] = wild_apps['Rating'].fillna(average_rating)
# Удаляем все приложение в которых хотя бы одна колонка пустая
wild_apps = wild_apps.dropna()

# Преобразуем цену в число $1.99 -> 1.99
def repair_price(price): # 0
    if '$' in price:
        return float(price[1:])
    else:
        return 0

wild_apps['Price'] = wild_apps['Price'].apply(repair_price)

print( wild_apps['Rating'].mean() )

# Преобразуем размер в число 20M 896k

def repair_size(size):
    if 'M' in size:
        return float(size[0:-1]) 
    elif 'k' in size:
        return float(size[0:-1]) / 1024 
    return 0

wild_apps['Size'] = wild_apps['Size'].apply(repair_size)
print( wild_apps['Size'].mean() )



