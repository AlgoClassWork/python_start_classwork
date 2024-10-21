import pandas 

apps = pandas.read_csv('GoogleApps.csv')
# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
temp =  apps['Category'].value_counts()
print(temp['BUSINESS'])
# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
temp = apps['Content Rating'].value_counts()
print(temp['Teen'] / temp['Everyone 10+'])
# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? 
temp = apps.groupby(by='Type')['Rating'].mean()
print(temp['Paid'])
# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
print(temp['Paid'] - temp['Free'])
# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
temp = apps.groupby(by='Category')['Size'].agg(['min','max'])
print(temp)
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
high_rating = apps [ (apps['Rating'] > 4.9 ) & (apps['Type'] == 'Free' )   ]
# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?

