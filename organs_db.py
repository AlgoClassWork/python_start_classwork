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

def add_organ(name, category, description, price, image):
    connection = sqlite3.connect('organs.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO organs (name, category, description, price, image)
    VALUES (?, ?, ?, ?, ?)
    ''',(name, category, description, price, image))

    connection.commit()
    connection.close()

create_database()
add_organ('Рука','Конечность','Сильная','100','')
