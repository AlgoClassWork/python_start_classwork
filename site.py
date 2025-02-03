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
<form action="/create" method="post">
    <input type="text" placeholder="Заголовок" name="name" required> <br>
    <textarea placeholder="Описание" name="description"></textarea> <br>
    <button type="submit">Создать</button>
</form>

{% for ad in ads %}
    <h1> {{ad[0]}} </h1>
    <p> {{ad[1]}} </p>
{% endfor %}

