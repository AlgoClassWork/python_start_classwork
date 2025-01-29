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

create_db()
