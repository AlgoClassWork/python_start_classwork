import pandas as pd
# Загрузка
def load_data(path):
    return pd.read_csv(path)
# Чистка данных
def clean_data(data):
    data['Revenue (Millions)'] = data['Revenue (Millions)'].fillna(-1)
    data['Metascore'] = data['Metascore'].fillna(-1)
    data['Runtime Category'] = pd.cut(data['Runtime (Minutes)'],
    bins=[0,90,120,150,180], labels=['Short','Medium','Long','Epic'])
    return data
