import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Загрузка данных
df = pd.read_csv("weatherData.csv")

# Подготовка данных
y = df['Summary']
X = df.drop(['date', 'Summary', 'Precip Type'], axis=1)

# Делим выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=42)

# Модели
models = {
    "KNN": KNeighborsClassifier(n_neighbors=11),
    "GaussianNB": GaussianNB(),
    "SGDClassifier": SGDClassifier(),
    "DecisionTree": DecisionTreeClassifier()
}

results = []

# Обучение и оценка
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cv_acc = cross_val_score(model, X, y, cv=5).mean()
    results.append((name, acc * 100, cv_acc * 100))

# Визуализация
labels, test_accs, cv_accs = zip(*results)
x = range(len(labels))
plt.figure(figsize=(10, 6))
plt.bar(x, test_accs, width=0.4, label='Test Accuracy', align='center')
plt.bar([i + 0.4 for i in x], cv_accs, width=0.4, label='CV Mean Accuracy', align='center')
plt.xticks([i + 0.2 for i in x], labels)
plt.ylabel("Accuracy (%)")
plt.title("Сравнение точности моделей")
plt.legend()
plt.tight_layout()
plt.show()
