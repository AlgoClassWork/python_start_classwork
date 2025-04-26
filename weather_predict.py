import pandas 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

data = pandas.read_csv('weatherData.csv')

def repair_summary(summary):
    summary = summary.lower()
    if 'cloud' in summary:
        return 'Cloudy'
    elif 'clear' in summary or 'sun' in summary:
        return 'Clear'
    else:
        return 'Other'

data['Summary'] = data['Summary'].apply(repair_summary)
data = data[ data['Summary'].isin(['Cloudy', 'Clear']) ]
# Разделяем данные на целевую переменную и признаки
y = data['Summary']
x = data.drop(['date', 'Precip Type', 'Summary'], axis=1)
# Разделяем данные на тренировачные и тестировачные
x = StandardScaler().fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
# Обучение модели KNN
model_knn = KNeighborsClassifier(n_neighbors=11)
model_knn.fit(x_train, y_train)
# Оценка качества KNN
y_pred = model_knn.predict(x_test) 
print('Результат KNN:', accuracy_score(y_test, y_pred) * 100, '%')

# Обучение модели Байеса
model_gauss = GaussianNB()
model_gauss.fit(x_train, y_train)
# Оценка качества Байеса
y_pred = model_gauss.predict(x_test) 
print('Результат Байеса:', accuracy_score(y_test, y_pred) * 100, '%')

