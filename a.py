import pandas 
import matplotlib.pyplot

data = pandas.read_csv('countries.csv')

# ПОДГОТОВКА ДАННЫХ
def repair(value):
    value = str(value)
    return float(value.replace(',','.'))

columns = ['Pop','Coastline','Migration','Mortality','Literacy',
           'Phones','Arable','Crops','Other','Climate','Birthrate',
           'Deathrate','Agriculture','Industry','Service','GDP']

for column in columns:
    data[column] = data[column].apply(repair)

for column in columns:
    data[column].fillna(data[column].mean(), inplace=True)

# АНАЛИЗ И ВИЗУАЛИЗАЦИЯ ДАННЫХ
# 1. Влияет ли уровень ВВП на грамотность населения
#data.plot(x='GDP', y='Literacy', kind='scatter')
# 2. Проверка числа стран по регионам
#data['Region'].value_counts().plot(kind='pie')
# 3. Статистика смертности по регионам
data.groupby('Region')['Deathrate'].mean().plot(kind='barh')

matplotlib.pyplot.show()
