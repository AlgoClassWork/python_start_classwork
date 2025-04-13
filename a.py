import pandas 
import matplotlib.pyplot

data = pandas.read_csv('countries of the world.csv')

# Подготовка данных
def repair(value):
    value = str(value)
    if ',' in value:
        return  float(value.replace(',','.'))
    return float(value)

data['Literacy'] = data['Literacy'].apply(repair)
data['Density'] = data['Density'].apply(repair)
data['Coastline'] = data['Coastline'].apply(repair)
data['Migration'] = data['Migration'].apply(repair)
data['Mortality'] = data['Mortality'].apply(repair)
data['Phones'] = data['Phones'].apply(repair)
data['Arable'] = data['Arable'].apply(repair)
data['Crops'] = data['Crops'].apply(repair)
data['Other'] = data['Other'].apply(repair)
data['Climate'] = data['Climate'].apply(repair)
data['Birthrate'] = data['Birthrate'].apply(repair)
data['Deathrate'] = data['Deathrate'].apply(repair)
data['Agriculture'] = data['Agriculture'].apply(repair)
data['Industry'] = data['Industry'].apply(repair)
data['Service'] = data['Service'].apply(repair)

data['Literacy'].fillna( data['Literacy'].median(), inplace=True )
data['Migration'].fillna( data['Migration'].median(), inplace=True )
data['Mortality'].fillna( data['Mortality'].median(), inplace=True )
data['GDP'].fillna( data['GDP'].median(), inplace=True )
data['Phones'].fillna( data['Phones'].median(), inplace=True )
data['Arable'].fillna( data['Arable'].median(), inplace=True )
data['Crops'].fillna( data['Crops'].median(), inplace=True )
data['Other'].fillna( data['Other'].median(), inplace=True )
data['Climate'].fillna( data['Climate'].median(), inplace=True )
data['Birthrate'].fillna( data['Birthrate'].median(), inplace=True )
data['Deathrate'].fillna( data['Deathrate'].median(), inplace=True )
data['Agriculture'].fillna( data['Agriculture'].median(), inplace=True )
data['Industry'].fillna( data['Industry'].median(), inplace=True )
data['Service'].fillna( data['Service'].median(), inplace=True )

# Анализ данных 

# Связь между ВВП и Уровнем Грамотности населения
#data.plot(x='GDP',y='Literacy', kind='scatter')
# Связь между ВВП и Уровнем Миграции населения
#data.plot(x='GDP',y='Migration', kind='scatter')
# Cвязь между ВВП и Детской смертностью
#data.plot(x='GDP',y='Mortality', kind='scatter')

matplotlib.pyplot.show()
