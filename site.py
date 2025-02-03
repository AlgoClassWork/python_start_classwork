#database.py
import sqlite3

def create_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ads (
    name TEXT NOT NULL,
    description TEXT)
    ''')
    connection.commit()
    connection.close()

def add(name, description):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO ads (name, description) VALUES (?, ?)', (name, description))
    connection.commit()
    connection.close()

def get_ads():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ads')
    data = cursor.fetchall()
    connection.close()
    return data






#main.py
from flask import Flask, render_template, request, redirect, url_for
from database import get_ads, add

app = Flask(__name__)

@app.route('/')
def index():
    ads = get_ads()
    return render_template('index.html', ads = ads )

@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    description = request.form.get('description')
    add(name, description)
    return redirect(url_for('index'))


app.run()


#index.html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

<div class="container">
    <form action="/create" method="post">
        <input type="text" placeholder="Заголовок" name="name" required> <br>
        <textarea placeholder="Описание" name="description"></textarea> <br>
        <button type="submit">Создать</button>
    </form>

    {% for ad in ads %}
        <div class="ad-card">
            <h1>{{ ad[0] }}</h1>
            <p>{{ ad[1] }}</p>
        </div>
    {% endfor %}
</div>


#style.css
/* Основной фон и шрифт страницы */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    color: #333;
    margin: 0;
    padding: 0;
}

/* Центрируем содержимое */
.container {
    width: 80%;
    max-width: 800px;
    margin: 40px auto;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Заголовки объявлений */
h1 {
    font-size: 24px;
    color: #2c3e50;
    margin-bottom: 10px;
}

/* Описание объявлений */
p {
    font-size: 16px;
    color: #7f8c8d;
    line-height: 1.5;
}

/* Стили для формы */
form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-bottom: 20px;
}

/* Внешний вид текстового поля и текстовой области */
input[type="text"],
textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
}

textarea {
    resize: vertical;
    min-height: 100px;
}

/* Кнопка */
button {
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 15px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #2980b9;
}

/* Стиль для каждой карточки объявления */
.ad-card {
    background-color: #ecf0f1;
    padding: 20px;
    margin-bottom: 15px;
    border-radius: 6px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

/* Заголовок объявления в карточке */
.ad-card h1 {
    font-size: 20px;
    color: #2c3e50;
}

/* Описание объявления в карточке */
.ad-card p {
    color: #7f8c8d;
    font-size: 14px;
}
  
