import pandas

data = pandas.read_csv('countries.csv')

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

print(data.info())
