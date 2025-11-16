import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from tqdm import tqdm

# === Загрузка данных ===
data = pd.read_csv('weatherData.csv')

# Разделяем признаки и цель
X = data.drop('Temperature (C)', axis=1)
y = data['Temperature (C)']

cat_features = ['Summary', 'Precip Type']
num_features = ['Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']

# === Препроцессинг ===
preprocess = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ]
)

# === Разделение без перемешивания ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, shuffle=False
)

# === Препроцессинг данных ===
# (т.к. мы будем обучать лес вручную, прогоняем данные отдельно)
X_train_prep = preprocess.fit_transform(X_train)
X_test_prep = preprocess.transform(X_test)

# === Настройки модели ===
n_trees = 1
model = RandomForestRegressor(
    n_estimators=1,
    warm_start=True,    # позволяет добавлять деревья
    max_depth=20,
    random_state=42,
    n_jobs=-1
)

print("Обучение модели...")

# === Обучение с прогресс-баром ===
for i in tqdm(range(1, n_trees + 1), desc="Процесс обучения"):
    model.n_estimators = i   # увеличиваем число деревьев
    model.fit(X_train_prep, y_train)

# === Оценка ===
pred = model.predict(X_test_prep)
print("MAE:", mean_absolute_error(y_test, pred))

# === Функция предсказания ===
def weather_predict(humidity, wind, pressure, summary, precip):
    df = pd.DataFrame([{
        'Humidity': humidity,
        'Wind Speed (km/h)': wind,
        'Pressure (millibars)': pressure,
        'Summary': summary,
        'Precip Type': precip
    }])
    df = preprocess.transform(df)
    prediction = model.predict(df)[0]
    print("Предполагаемая температура:", prediction)


weather_predict(1, 100, 1000, 'Clear', 'rain')
