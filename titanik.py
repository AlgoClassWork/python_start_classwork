import pandas 
#pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# Подготовка данных для построения математической модели
data = pandas.read_csv('titanic.csv')

data = data.drop(['PassengerId','Name','Ticket','Fare','Cabin','Embarked'], axis=1)

data['Age'] = data['Age'].fillna( data['Age'].mean() )

def repair_gender(gender):
    if gender == 'male':
        return 1
    return 0
    
data['Sex'] = data['Sex'].apply( repair_gender )

# Создание математической модели для предсказаний
# Этап 1 Разделение признаков (возраст пол и тд) и цели (итог выживания)
info = data.drop('Survived', axis=1)
goal = data['Survived']
# Этап 2 Разделение данных на обучающие и тестировачные
info_train, info_test, goal_train, goal_test = train_test_split(info, goal, test_size=0.3)
# Этап 3 (Опционально) Работа с масштабированием данных
scaler = StandardScaler()
info_train = scaler.fit_transform( info_train )
info_test = scaler.transform( info_test )
# Этап 4 Обучение нашей модели
model = KNeighborsClassifier(n_neighbors=3)
model.fit(info_train, goal_train)
# Этап 5 Оценка точности нашей модели
goal_prediction = model.predict(info_test)
print('Точность предсказаний:', accuracy_score(goal_test, goal_prediction))

# Функция для предсказания судьбы выдуманного пассажира
def fate_predict( passanger ):
    passanger = scaler.transform(passanger)
    prediction = model.predict(passanger)[0]
    chance = model.predict_proba(passanger)[0]
    print('Судьба пассажира:', 'Выжил' if prediction == 1 else 'Умер')
    print(f'Шанс на выживание {round(chance[1] * 100,2)}%')

fate_predict( [[1, 1, 40, 0, 0]] )
