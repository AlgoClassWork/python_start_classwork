import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Загрузка
def load_data(path):
    return pd.read_csv(path)
# Чистка данных
def clean_data(data):
    data['Revenue (Millions)'] = data['Revenue (Millions)'].fillna(-1)
    data['Metascore'] = data['Metascore'].fillna(-1)
    data['Runtime Category'] = pd.cut(data['Runtime (Minutes)'],
    bins=[0,90,120,150,180], labels=['Short','Medium','Long','Epic'])
    return data

def plot_box(data, x, y, title, xlabel, ylabel):
    plt.figure()
    sns.boxplot(x=x, y=y, data=data, palette='pastel')
    plt.title(title, fontsize=20, fontweight='bold')
    plt.xlabel(xlabel=xlabel, fontsize=15)
    plt.ylabel(ylabel=ylabel, fontsize=15)
    plt.show()

def plot_scatter(data, x, y, title, xlabel, ylabel):
    plt.figure()
    sns.scatterplot(x=x, y=y, data=data, palette='pastel')
    plt.title(title, fontsize=20, fontweight='bold')
    plt.xlabel(xlabel=xlabel, fontsize=15)
    plt.ylabel(ylabel=ylabel, fontsize=15)
    plt.show()

# Получение готовых данных
data = load_data('IMDB-Movie-Data.csv')
data = clean_data(data)
# 1. Долгие фильмы имеют более высокий рейтинг
plot_box(data, 'Runtime Category', 'Rating',
'Рейтинг по категориям продолжительности','Категория','Рейтинг')
# 2. Рейтинг влияет на количество отзывов
plot_scatter(data, 'Rating', 'Votes',
'Связь между рейтингом и количеством отзывов','Рейтинг','Количество отзывов')
