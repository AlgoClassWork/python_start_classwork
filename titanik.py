import pandas


data = pandas.read_csv('titanic.csv')

age_1 = data[ data['Pclass'] == 1 ]['Age'].median()
age_2 = data[ data['Pclass'] == 2 ]['Age'].median()
age_3 = data[ data['Pclass'] == 3 ]['Age'].median()

def fill_age(row):
    if pandas.isnull( row['Age'] ):
        if row['Pclass'] == 1:
            return age_1
        if row['Pclass'] == 2:
            return age_2
        if row['Pclass'] == 3:
            return age_3
    else:
        return row['Age']
    
def fill_sex(sex):
    if sex == 'male':
        return 1
    else:
        return 0

data['Age'] = data.apply(fill_age, axis = 1)
data['Sex'] = data['Sex'].apply(fill_sex)

data.drop(['PassengerId','Pclass','Name','Ticket','Fare','Cabin','Embarked'],
          axis=1, inplace=True)
