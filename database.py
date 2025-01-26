import sqlite3

def create_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute ( '''
    CREATE TABLE IF NOT EXISTS ads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT)  ''' )
    connection.commit()
    connection.close()

def create_ad(name, description):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute ( '''
    INSERT INTO ads (name, description) VALUES (?,?) ''',(name, description))
    connection.commit()
    connection.close()

def get_ads():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute ('SELECT * FROM ads')
    ads = cursor.fetchall()
    connection.close()
    return ads




#pip install flask
from flask import Flask, render_template
import data

app = Flask(__name__)
data.create_db()

@app.route('/')
def index():
    ads = data.get_ads()
    return render_template('index.html', ads=ads)

app.run()





<form action="/create" method="post">
    <input type="text" name="name"><br>
    <textarea name="description"></textarea><br>
    <button type="submit">Отправить</button>
</form>

{% for ad in ads %}
    <h2>{{ ad[1] }}</h2>
    <p>{{ ad[2] }}</p>
{% endfor %}
