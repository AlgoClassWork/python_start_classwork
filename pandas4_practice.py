import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Выведи на экран минимальный, средний и максимальный рейтинг ('Rating') платных и бесплатных приложений ('Type') с точностью до десятых.
print( df.groupby(by='Type')['Rating'].agg(['min','mean','max'])    )
# 2 Выведи на экран минимальную, медианную (median) и максимальную цену ('Price') платных приложений (Type == 'Paid') для 
# разных целевых аудиторий ('Content Rating')
paid = df[ df['Type']=='Paid' ]
print(paid.groupby(by='Content Rating')['Price'].agg(['min','median','max'])   )
# 3 Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом
#print(df.groupby(by=['Content Rating','Category'])['Reviews'].max())
print( df.pivot_table(
    index='Category',
    columns='Content Rating',
    values='Reviews',
    aggfunc='max'
)  )

# 4 Сгруппируй платные (Type == 'Paid') приложения по категории ('Category') и целевой аудитории ('Content Rating')
# Посчитай среднее количество отзывов ('Reviews') в каждой группе
# Обрати внимание, что в некоторых ячейках полученной таблицы отражается не число, а значение "NaN" - Not a Number
# Эта запись означает, что в данной группе нет ни одного приложения.
# Выбери названия категорий, в которых есть платные приложения для всех возрастных групп и расположи их в алфавитном порядке.

# Бонусная задача. Найди категории бесплатных (Type == 'Free') приложений, 
# в которых приложения разработаны не для всех возрастных групп ('Content Rating')
