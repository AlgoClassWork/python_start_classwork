import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('StudentsPerformance.csv')
print(data.info())



data['total score'] = data["math score"] + data["reading score"] + data["writing score"]
male = data[ data['gender'] == 'male' ]
result =  male.groupby(by='lunch')['total score'].mean()

result.plot(kind='pie')
plt.show()


