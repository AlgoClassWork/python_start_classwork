import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')
df['total'] = df['writing score'] + df['reading score'] + df['math score']
data = df.groupby('test preparation course')['total'].mean()
print(data)

# Группируем по столбцу "gender"
gender_group = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
print(gender_group)
# Визуализация
gender_group.plot(kind='bar')
plt.show()

# Группируем по уровню образования родителей
education_group = df.groupby("parental level of education")['total'].mean()
print(education_group)
# Визуализация
education_group.plot(kind='bar')
plt.show()


# Группируем по столбцу "lunch"
lunch_group = df.groupby("lunch")['total'].mean()
print(lunch_group)
# Визуализация
lunch_group.plot(kind='bar')
plt.show()


# Группируем данные по этнической принадлежности
ethnicity_group = df.groupby("race/ethnicity")['total'].mean()
print(ethnicity_group)
# Визуализация
ethnicity_group.plot(kind='bar')
plt.show()
