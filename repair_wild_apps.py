import pandas 
# Извлечение данных
wild_apps = pandas.read_csv('wild_apps.csv')
# Подготовка данных
# Заменить пустоту в колонке рейтинг на среднее значение
average_rate = wild_apps['Rating'].mean() 
wild_apps['Rating'] = wild_apps['Rating'].fillna( average_rate )
# Удалить приложения в которых остались пустые колонки
wild_apps = wild_apps.dropna()

# Чиним колонку с размерами приложений превращаем строку '5.6M' в дробь 5.6
def repair_size(size): # size = '5.6M'
    if 'M' in size:
        return float( size[0:-1] ) # 5.6
    elif 'k' in size:
        return float( size[0:-1] ) / 1024
    return 0
    
wild_apps['Size'] = wild_apps['Size'].apply( repair_size )

# Чиним колонку с ценами приложений превращаем строку '$0.99' в дробь 0.99
def repair_price(price): # price = '$0.99'
    if '$' in price:
        return float(price[1:]) # 0.99
    return 0

wild_apps['Price'] = wild_apps['Price'].apply( repair_price )

wild_apps.info()



