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


# CОЗДАНИЕ МАТЕМАТИЧЕСКОЙ МОДЕЛИ
# pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# Разделение признаков (возраст пол и тд) и целевой переменной (итог выживания)
x = data.drop('Survived', axis=1)
y = data['Survived']
# Разделение данных на те что будут обучать модель и на те что будут ее тестировать
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# Мастштабирование наших данных (превращаем числа в проценты)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# Обучение нашей математической модели
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)
# Оценка качества нашей модели
y_pred = model.predict(x_test) 
print('Точность предсказаний на тестовых данных', int(accuracy_score(y_test, y_pred) * 100), '%')
