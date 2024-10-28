import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')

print( len(df[pd.isnull(df['Rating'])]) ) #1 задание

df['Rating'].fillna(-1, inplace=True) # 2 задание

print(df['Size'].value_counts()) # 3 задание
def fix_size(size):
    if size[-1] == 'M':
        return  float(size[:-1])
    elif size[-1] == 'k':
        return  float(size[:-1]) / 1024
    return -1

df['Size'] = df['Size'].apply(fix_size)

print(  df[df['Category'] == 'TOOLS']['Size'].max()  ) # 4 задание
# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
def fix_install(install):
    if install == '0':
        return 0
    return int(install[:-1].replace(',',''))

df['Installs'] = df['Installs'].apply(fix_install)
# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000

# Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
# посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением. 
# К какой возрастной группе и типу приложений относятся данные из этой ячейки?

# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?

# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно
