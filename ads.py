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
from flask import Flask, render_template, request, redirect, url_for
from data import get_ads, create_ad

app = Flask(__name__)

@app.route('/')
def index():
    ads = get_ads()
    return render_template('index.html', ads=ads)

@app.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('description')
    create_ad(title, content)
    return redirect(url_for('index'))

app.run()
#index.html
<link rel="stylesheet" href="static/style.css">

<h1 class="page-title">Доска объявлений</h1>

<!-- Форма для создания объявления -->
<form action="/create" method="post" class="form-container">
    <input type="text" placeholder="Заголовок" name="title" class="input-field" required> <br>
    <textarea placeholder="Описание" name="description" class="input-field" required></textarea> <br>
    <button type="submit" class="submit-button">Создать</button>
</form>

<!-- Список объявлений -->
<div class="ads-container">
    {% for ad in ads %}
        <div class="ad">
            <h2 class="ad-title">{{ ad[0] }}</h2>
            <p class="ad-description">{{ ad[1] }}</p>
        </div>
    {% endfor %}
</div>

#style.css

/* Общие стили */
body {
    font-family: 'Roboto', sans-serif;
    background-color: #f0f0f0;
    color: #333;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    height: 100vh;
    flex-direction: column;
}

.page-title {
    text-align: center;
    color: #333;
    font-size: 36px;
    margin-top: 20px;
}

/* Стили для формы */
.form-container {
    background-color: #fff;
    padding: 20px;
    margin-top: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    max-width: 500px;
    width: 100%;
    margin-bottom: 30px;
}

.input-field {
    width: 100%;
    padding: 12px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    box-sizing: border-box;
    background-color: #fafafa;
}

textarea {
    resize: vertical;
    height: 100px;
}

/* Кнопка */
.submit-button {
    width: 100%;
    padding: 12px;
    background-color: #4CAF50;
    border: none;
    color: white;
    font-size: 16px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
    box-sizing: border-box;
}

.submit-button:hover {
    background-color: #45a049;
}

/* Стили для списка объявлений */
.ads-container {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
}

.ad {
    background-color: #fff;
    padding: 20px;
    margin-bottom: 15px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.ad-title {
    font-size: 24px;
    margin-bottom: 10px;
    color: #333;
}

.ad-description {
    font-size: 16px;
    color: #555;
}

