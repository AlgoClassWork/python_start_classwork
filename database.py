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








#pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run()
