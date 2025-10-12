import pandas 
# Извлечение данных
apps = pandas.read_csv('apps.csv')
# Информация о таблице
apps.info()
# Вывести всю таблицу
print( apps )
# Вывести одну колонку таблицы (Названия)
print( apps['App'] )
# Вывести средний рейтинг всех приложений
print( apps['Rating'].mean() )
# Вывести все дорогие приложения (дороже 100 баксов)
print( apps[ apps['Price'] > 99 ] )
# Вывести кол-во отзывов всех приложений для знакомств
print( apps[ apps['Category'] == 'DATING' ]['Reviews'] )
# Вывести медианный размер среди игр
print( apps[ apps['Category'] == 'GAME' ]['Size'].median() )
# Вывести все приложения которые весят больше 50 мб и стоят дешевле 20 долларов
print( apps[ ( apps['Size'] > 99 ) & ( apps['Price'] < 20 ) ] )
# Вывести названия всех приложения которые скачивали больше 10000 раз и их рейтинг выше 4.5
print( apps[ ( apps['Installs'] > 100000 ) & ( apps['Rating'] > 4.8 ) ]['App'] )
# Вывести среднее количество оценок всех приложения которые весят меньше 1 мб и они платные
print( apps[ ( apps['Type'] == 'Paid' ) & ( apps['Size'] < 1 ) ]['Reviews'].mean() )
