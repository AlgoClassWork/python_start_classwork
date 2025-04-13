import pandas 

data = pandas.read_csv('countries.csv')

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

print(data.info())
