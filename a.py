import pandas 
import matplotlib.pyplot as plt
import seaborn as sns

data = pandas.read_csv('student.csv')

data['final score'] = data['math score'] + data['reading score'] + data['writing score']

# Гипотеза 1. хождение на курсы увеличивает итоговый балл
#hypo1 =  data.groupby('test preparation course')['final score'].median()
#hypo1.plot(kind='bar')
# Гипотеза 2. влияет ли еда успешную сдачу экзамена
#hypo2 = data.groupby('lunch')['final score'].mean()
sns.boxplot(x='gender',y='final score',hue='lunch',data=data, palette='Set1')
plt.show()
