import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# Извлечение данных
data = pandas.read_csv('weatherData.csv')
# Разделение данных на целевую переменную и признаки
y = data['Summary']
x = data.drop(['date', 'Summary', 'Precip Type'], axis=1)
# Разделение данных на тренировачные и тестовые
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.9)
# Масштабирование данных
#scaler = StandardScaler()
#x_train = scaler.fit_transform(x_train)
#x_test = scaler.transform(x_test)
# Создание и обучение модели (KNN)
model_knn = KNeighborsClassifier(n_neighbors=11)
model_knn.fit(x_train, y_train)
# Оценка точности предсказаний (KNN)
y_pred = model_knn.predict(x_test)
print('Точность предсказаний алгоритма KNN', accuracy_score(y_test, y_pred) * 100, '%')
# Создание и обучение модели (Байеса)
model_gauss = GaussianNB()
model_gauss.fit(x_train, y_train)
# Оценка точности предсказаний (Байеса)
y_pred = model_gauss.predict(x_test)
print('Точность предсказаний алгоритма Байеса', accuracy_score(y_test, y_pred) * 100, '%')
# Создание и обучение модели (SGD)
model_sgd = SGDClassifier()
model_sgd.fit(x_train, y_train)
# Оценка точности предсказаний (SGD)
y_pred = model_sgd.predict(x_test)
print('Точность предсказаний алгоритма SGD', accuracy_score(y_test, y_pred) * 100, '%')
# Создание и обучение модели (Tree)
model_tree = DecisionTreeClassifier()
model_tree.fit(x_train, y_train)
# Оценка точности предсказаний (Tree)
y_pred = model_tree.predict(x_test)
print('Точность предсказаний алгоритма Tree', accuracy_score(y_test, y_pred) * 100, '%')
