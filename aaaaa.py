import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('GoogleApps.csv')

size_info = data['Size']
size_info.plot(kind='hist')

plt.show()
