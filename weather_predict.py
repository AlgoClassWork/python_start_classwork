import pandas 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.metrics import mean_absolute_error

# Подготовка данных для построения математической модели
data = pandas.read_csv('weatherData.csv')
data = data.drop(['date','Summary','Precip Type'], axis=1)
# Создание математической модели для предсказаний
# Этап 1 Разделение признаков (ветер, влажность, давление) и цели (температура)
info = data.drop('Temperature (C)', axis=1)
goal = data['Temperature (C)']
# Этап 2 Разделение данных на обучающие и тестировачные
info_train, info_test, goal_train, goal_test = train_test_split(info, goal, test_size=0.1)
# Этап 3 (Опционально) Работа с масштабированием данных
scaler = StandardScaler()
info_train = scaler.fit_transform( info_train )
info_test = scaler.transform( info_test )
# Этап 4 Обучение нашей модели
model = KNeighborsRegressor()
model.fit(info_train, goal_train)
# Этап 5 Оценка точности нашей модели
goal_prediction = model.predict(info_test)
print('В среднем модель ошибается на', mean_absolute_error(goal_test, goal_prediction), 'градусов')
