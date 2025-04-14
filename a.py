import pandas
import matplotlib.pyplot

data = pandas.read_csv('countries.csv')

# Подготовка данных
def repair(value):
    value = str(value)
    return float(value.replace(',','.'))

columns = ['Density','Coastline','Migration','Mortality','GDP',
           'Literacy','Phones','Arable','Crops','Other','Climate',
           'Birthrate','Deathrate','Agriculture','Industry','Service']

for column in columns:
    data[column] = data[column].apply( repair )

for column in columns:
    data[column] = data[column].fillna( data[column].mean() )

# АНАЛИЗ ДАННЫХ
# Гипотеза 1 ВВП зависит от уровня Грамотности населения
# Сложный способ 
def do_wealth(gdp):
    if gdp < 15000:
        return 'poor'
    elif gdp >= 15000 and gdp <= 30000:
        return 'normal'
    else:
        return 'rich'

data['Wealth'] = data['GDP'].apply(do_wealth)
print(data.groupby('Wealth')['Literacy'].mean())
# Простой способ
data.plot(x='GDP', y='Literacy', kind='scatter')

matplotlib.pyplot.show()
