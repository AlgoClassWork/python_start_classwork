import sqlite3

def create_db():
    connection = sqlite3.connect('ads.db')
    cursor = connection.cursor()
    cursor.execute ('''
    CREATE TABLE IF NOT EXISTS ads (
    name TEXT NOT NULL,
    description TEXT) ''')
    connection.commit()
    connection.close()

def create_ad(name, description):
    connection = sqlite3.connect('ads.db')
    cursor = connection.cursor()
    cursor.execute ('''
    INSERT INTO ads (name, description) VALUES (?, ?)''', (name, description))
    connection.commit()
    connection.close()

def get_ads():
    connection = sqlite3.connect('ads.db')
    cursor = connection.cursor()
    cursor.execute ('SELECT * FROM ads')
    ads = cursor.fetchall()
    connection.close()
    return ads

create_db()
#create_ad('Пропала собака', 'Вес 100кг Алабай не кусается')
#create_ad('Нашел собаку', 'Верну за вознаграждение')


#main.py
from flask import Flask, render_template
from data import get_ads

app = Flask(__name__)

@app.route('/')
def index():
    ads = get_ads()
    return render_template('index.html', ads=ads)

app.run()

#index.html
<h1> Доска обьявлений! </h1>

<form action="/create" method="post">
    <input type="text" placeholder="Заголовок" name="title"> <br>
    <input type="text" placeholder="Описание" name="description"> <br>
    <button type="submit">Создать</button>
</form>

{% for ad in ads %}
    <h2> {{ ad[0] }} </h2>
    <p>Описание: {{ ad[1] }} </p>
{% endfor %}

