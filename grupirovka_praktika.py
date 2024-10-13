import pandas as pd
apps = pd.read_csv('GoogleApps.csv')

#new_tab = data_frame['Content Rating'].value_counts()

#print(data_frame.groupby(by=['Android Ver'])['Rating'].agg(['mean','max']) )

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
buisness = apps['Category'].value_counts()
print(buisness['BUSINESS'])
# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
auditoria = apps['Content Rating'].value_counts()
teen = auditoria['Teen']
ten_plus = auditoria['Everyone 10+']
print(ten_plus/teen)
# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? 
# Ответ запиши с точностью до сотых.
type =  apps.groupby(by='Type')['Rating'].mean()
free = type['Free']
paid = type['Paid']
print('Разница в рейтинге составляет',paid - free)
# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.

# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
print(apps.groupby(by=['Category'])['Size'].agg(['min','max']))
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
print(apps[apps['Rating'] > 4.5]['Category'].value_counts())
# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
data = apps[(apps['Category']== 'GAME') & (apps['Rating'] > 4.9)]['Type'].value_counts()
print(data)
