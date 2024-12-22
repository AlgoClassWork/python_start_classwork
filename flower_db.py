import sqlite3

def create_database():
    connection = sqlite3.connect('flowers.db')
    cursor = connection.cursor()
    cursor.execute(     '''
    CREATE TABLE IF NOT EXISTS flowers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL,
    quantity INTEGER,
    image_path TEXT)    ''')
    connection.commit()
    connection.close()

create_database()
