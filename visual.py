import pandas
import matplotlib.pyplot as render

df = pandas.read_csv('GoogleApps.csv')

# ГИСТОГРАММА
size = df['Rating']
grafik = size.plot(kind='hist',bins=20)

render.show()

#pip install matplotlib
