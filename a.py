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
#sns.boxplot(x='gender',y='final score',hue='lunch',data=data, palette='Set1')
# Распределение итоговых баллов
sns.histplot(data['final score'],kde=True, color='orange',bins=20)
plt.title('Распределение баллов', fontsize=20)
plt.xlabel('Итоговый балл')
plt.ylabel('Частота')
plt.tight_layout()

hypo = data.groupby('race/ethnicity')['final score'].mean()
sns.barplot(x=hypo.index, y=hypo.values, palette="Set2")
plt.tight_layout()

corr = data[['math score','reading score', 'writing score', 'final score']].corr()
sns.heatmap(corr)

plt.show()
