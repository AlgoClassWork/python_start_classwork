import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# === Загрузка данных ===
data = pd.read_csv('weatherData.csv')

# Разделяем признаки и цель
X = data.drop('Temperature (C)', axis=1)
y = data['Temperature (C)']

# Категориальные признаки
cat_features = ['Summary', 'Precip Type']

# Числовые признаки
num_features = ['Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']

# === Препроцессинг ===
preprocess = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ]
)

# === Модель ===
model = RandomForestRegressor(
    n_estimators=300,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)

# === Конвейер ===
pipeline = Pipeline(steps=[
    ('preprocess', preprocess),
    ('model', model)
])

# === Разделение без перемешивания, чтобы учитывать время ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, shuffle=False
)

# === Обучение ===
pipeline.fit(X_train, y_train)

# === Оценка качества ===
pred = pipeline.predict(X_test)
print("MAE:", mean_absolute_error(y_test, pred))

# === Функция предсказывания ===
def weather_predict(humidity, wind, pressure, summary, precip):
    df = pd.DataFrame([{
        'Humidity': humidity,
        'Wind Speed (km/h)': wind,
        'Pressure (millibars)': pressure,
        'Summary': summary,
        'Precip Type': precip
    }])
    prediction = pipeline.predict(df)[0]
    print("Предполагаемая температура:", prediction)

weather_predict(0.82, 1, 1000, "Partly Cloudy", "rain")
