import sqlite3

def create_database():
    connection = sqlite3.connect('organs.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS organs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    description TEXT,
    price INTEGER,
    image TEXT)  ''')

    connection.commit()
    connection.close()

create_database()
