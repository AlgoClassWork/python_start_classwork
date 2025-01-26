#index.html

<h1>Список учеников:</h1>

<ul>
    {% for name in names  %}
        <li>{{name[1]}} {{name[2]}}</li>
    {% endfor %}
</ul>

<h1>Добавить ученика</h1>

<form action="/create" method="post">
    <input type="text" name="name" placeholder="Имя:">
    <input type="text" name="surname" placeholder="Фамилия:">
    <button type="submit">Добавить</button>
</form>


#data.py
import sqlite3

def create_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS names 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL)
    ''')
    connection.commit()
    connection.close()

def add_name(name, surname):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO names (name, surname) VALUES (?, ?)', (name, surname) )
    connection.commit()
    connection.close()

def get_name():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(' SELECT * FROM names ')
    data = cursor.fetchall()
    connection.close()
    return data



#main.py
#pip install flask
from flask import Flask, render_template, request, redirect, url_for
from data import get_name, create_db, add_name

app = Flask(__name__)
create_db()


@app.route('/')
def index():
    names = get_name()
    return render_template('index.html',names=names)

@app.route('/create', methods=['POST'])
def add():
    name = request.form.get('name')
    surname = request.form.get('surname')
    add_name(name, surname)
    return redirect(url_for('index'))

app.run()
