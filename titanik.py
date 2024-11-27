# Здесь должен быть твой код
import pandas as pd

data = pd.read_csv('titanic.csv')

data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis = 1, inplace = True)

def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return data[data['Pclass'] == 1]['Age'].mean()
        if row['Pclass'] == 2:
            return data[data['Pclass'] == 2]['Age'].mean()
        if row['Pclass'] == 3:
            return data[data['Pclass'] == 3]['Age'].mean()
    return row['Age']

data['Age'] = data.apply(fill_age, axis=1)

def fill_gender(gender):
    if gender == 'male':
        return 1
    return 0

data['Sex'] = data['Sex'].apply(fill_gender)

print(data.info())
