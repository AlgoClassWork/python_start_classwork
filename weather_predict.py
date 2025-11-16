
import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Подготовка данных
data = pandas.read_csv('weatherData.csv')

# Целевая переменная — Температура
goal = data['Temperature (C)']

# Признаки — Влажность, Скорость ветра, Давление
info = data[['Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']]

# Масштабирование признаков
scaler = StandardScaler()
info = scaler.fit_transform(info)

# Разделение на тренировочный и тестовый набор
info_train, info_test, goal_train, goal_test = train_test_split(
    info, goal, test_size=0.1, random_state=42
)

# Обучение модели
model = LinearRegression()
model.fit(info_train, goal_train)

# Пример входных данных
input_data = pandas.DataFrame({
    'Humidity': [1],
    'Wind Speed (km/h)': [100],
    'Pressure (millibars)': [1000]
})

input_data = scaler.transform(input_data)

# Предсказание
prediction = model.predict(input_data)
goal_prediction = model.predict(info_test)

# Метрики регрессии
mae = mean_absolute_error(goal_test, goal_prediction)
mse = mean_squared_error(goal_test, goal_prediction)
rmse = np.sqrt(mse)
r2 = r2_score(goal_test, goal_prediction)

print('Предсказанная температура:', prediction)
print(f'В среднем модель ошибается на {mae:.3f} °C (MAE)')
print(f'Средняя квадратичная ошибка модели: {mse:.3f}')
print(f'Обычно ошибка прогноза составляет около {rmse:.3f} °C (RMSE)')
print(f'Модель объясняет {r2:.1%} разброса данных (R²)')

