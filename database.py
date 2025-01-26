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
