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

def add_flower(name, description, price, quantity , image_path):
    connection = sqlite3.connect('flowers.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO flowers (name, description, price, quantity, image_path)
    VALUES (?, ?, ?, ?, ?)''',(name, description, price, quantity, image_path))
    connection.commit()
    connection.close()


create_database()
add_flower('Роза', 'Колючая', '500', '15', ' ')
add_flower('Орхидея', 'Черная', '1500', '8', ' ')
