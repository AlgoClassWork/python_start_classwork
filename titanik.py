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

# Разделение на признаки и целевую переменную
# pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

X = data.drop('Survived', axis=1)
Y = data['Survived']
# Разделение данных на обучающие и тестовые
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)
# Изменяем масштаб данных
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
# Обучение нашей модели
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train_scaled, y_train)
# Предсказания и оценка точности нашей модели
y_pred = model.predict(x_test_scaled)

print('Точность на тестовой выборке:', accuracy_score(y_test, y_pred) * 100, '%')
print('Матрица ошибок:\n', confusion_matrix(y_test, y_pred))
print('Отчет по классам:\n', classification_report(y_test, y_pred))

# Предсказание судьбы одного пассажира

def predict_single_passenger(passenger_info): 

    scaled = scaler.transform(passenger_info)
    prediction = model.predict(scaled)[0]
    probs = model.predict_proba(scaled)[0]

    print('Новый пассажир:', passenger_info)
    print('Предсказание', 'Выжил' if prediction == 1 else 'Не выжил')
    print(f'Уверенность: Не выжил - {int(probs[0] * 100)}% Выжил - {int(probs[1] * 100)}%')

predict_single_passenger( [[0,10,1,1]] )
