import sqlite3

def create_db():
    connection = sqlite3.connect('ads.db')
    cursor = connection.cursor()
    cursor.execute ('''
    CREATE TABLE IF NOT EXISTS ads (
    name TEXT NOT NULL,
    description TEXT) ''')
    connection.commit()
    connection.close()

def create_ad(name, description):
    connection = sqlite3.connect('ads.db')
    cursor = connection.cursor()
    cursor.execute ('''
    INSERT INTO ads (name, description) VALUES (?, ?)''', (name, description))
    connection.commit()
    connection.close()

def get_ads():
    connection = sqlite3.connect('ads.db')
    cursor = connection.cursor()
    cursor.execute ('SELECT * FROM ads')
    ads = cursor.fetchall()
    connection.close()
    return ads

create_db()
#create_ad('Пропала собака', 'Вес 100кг Алабай не кусается')
#create_ad('Нашел собаку', 'Верну за вознаграждение')
