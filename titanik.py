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

# ПОСТРОЕНИЕ МАТЕМАТИЧЕСКОЙ МОДЕЛИ
#pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Разделение на признаки и целевую переменную
X = data.drop('Survived', axis=1)
Y = data['Survived']
# Разделение на обучующие и тестовые данные
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.5)
# Масштабирование данных 
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
# Обучение модели
model = KNeighborsClassifier(n_neighbors=7)
model.fit(x_train_scaled, y_train)
# Оценка точности модели
y_pred = model.predict(x_test_scaled) 
print('Точность на тестовой выборке', accuracy_score(y_test, y_pred) * 100, '%' )
# Функция для предсказания судьбы нашего пассажира
def predict_my_passenger(passenger_info):

    info = scaler.transform(passenger_info)
    predict = model.predict(info)[0]
    proba = model.predict_proba(info)[0]

    print('Предсказание:', 'Выжил' if predict == 1 else 'Умер' )
    print(f'Вероятность:\nСмерти - {proba[0]*100}%\nВыживания - {proba[1]*100}%')

predict_my_passenger( [[0, 25, 2, 2]] )
