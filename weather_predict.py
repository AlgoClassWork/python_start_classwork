import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pandas.read_csv('weatherData.csv')

y = data['Summary']
x = data.drop(['date', 'Summary', 'Precip Type'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model_knn = KNeighborsClassifier(n_neighbors=11)
model_knn.fit(x_train, y_train)

y_pred = model_knn.predict(x_test)
print('Точность предсказаний', accuracy_score(y_test, y_pred) * 100, '%')
