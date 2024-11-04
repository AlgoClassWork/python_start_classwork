import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('GoogleApps.csv')

# Гистограмма
#size_info = data['Size']
#size_info.plot(kind='hist')
# Ящик с усами 
#paid = data[data['Type'] == 'Free']['Rating']
#paid.plot(kind='box')
# Диаграма Рассеяния
#data.plot(x = 'Installs', y = 'Size', kind='scatter')
# Круговая диаграма
#category = data['Category'].value_counts().nlargest(10)
#content = data['Content Rating'].value_counts()
#category.plot(kind='pie')

plt.show()
