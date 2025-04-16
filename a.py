import pandas 

data = pandas.read_csv('titanic.csv')

age1 = data[data['Pclass'] == 1]['Age'].mean()
age2 = data[data['Pclass'] == 2]['Age'].mean()
age3 = data[data['Pclass'] == 3]['Age'].mean()

def repair_age(row):
    if pandas.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age1
        if row['Pclass'] == 2:
            return age2
        return age3
    return row['Age']

def repair_gender(gender):
    if gender == 'male':
        return 1
    return 0

data['Age'] = data.apply(repair_age , axis=1)
data['Sex'] = data['Sex'].apply( repair_gender )

data.drop(['PassengerId', 'Pclass', 'Name',
           'Ticket','Fare','Cabin','Embarked'],
           axis=1, inplace=True)

print(data['Sex'].value_counts())
