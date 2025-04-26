import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Загрузка данных
df = pd.read_csv("./weatherData.csv")

# Упрощаем Summary до 4 категорий
def simplify_summary(s):
    s = s.lower()
    if 'rain' in s:
        return 'Rainy'
    elif 'snow' in s:
        return 'Snowy'
    elif 'cloud' in s:
        return 'Cloudy'
    elif 'clear' in s or 'sun' in s:
        return 'Clear'
    else:
        return 'Other'

df['SimpleSummary'] = df['Summary'].apply(simplify_summary)

# Удаляем ненужные столбцы
X = df.drop(['date', 'Summary', 'SimpleSummary', 'Precip Type'], axis=1)
y = df['SimpleSummary']

# Нормализация
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Список моделей
models = {
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000)
}

# Обучение и оценка каждой модели
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cv_scores = cross_val_score(model, X_scaled, y, cv=5)
    print(f"{name} Accuracy: {acc:.3f}")
    print(f"{name} Cross-Validation Mean Accuracy: {cv_scores.mean():.3f}")
    print("-" * 40)
