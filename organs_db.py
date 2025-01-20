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

def delete_organ(id):
    connection = sqlite3.connect('organs.db')
    cursor = connection.cursor()

    cursor.execute('''DELETE FROM organs WHERE id=? ''', (id))

    connection.commit()
    connection.close()

def update_organ(name, category, description, price, image, id):
    connection = sqlite3.connect('organs.db')
    cursor = connection.cursor()

    cursor.execute('''UPDATE organs SET name=?, category=?, description=?, price=?, image=?
                   WHERE id=?''', (name, category, description, price, image, id))

    connection.commit()
    connection.close()

def get_all_organs():
    connection = sqlite3.connect('organs.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM organs ')
    data = cursor.fetchall()
    connection.close()
    return data

create_database()

add_organ('Рука', 'Конечность', 'Сильная, как сталь, идеально подходит для работы', '100', 'рука.jpg')
add_organ('Нога', 'Конечность', 'Мощная и устойчивая, не подведет в любой ситуации', '120', 'нога.jpg')
add_organ('Сердце от робота', 'Искусственные органы', 'Не перегревается, не выходит из строя', '9999', 'сердце_робота.jpg')
add_organ('Глаз киборга', 'Искусственные органы', 'Ультра-ясное зрение, ночное видение и Wi-Fi', '1500', 'глаз_киборга.jpg')
add_organ('Печень для оптимистов', 'Органы', 'Не боится праздников, выдержит любые тесты', '4999', 'печень.jpg')
add_organ('Мозг нейро-плант', 'Органы', 'Растение с нейро-системой, обучаемое и отзывчивое', '2999', 'мозг_плант.jpg')
add_organ('Легкие вентилятора', 'Органы', 'Мгновенно очищает воздух вокруг', '800', 'легкие_вентилятора.jpg')
add_organ('Желудок с GPS', 'Органы', 'Не потеряется, если вдруг окажется в неизвестном месте', '1200', 'желудок_gps.jpg')
add_organ('Роботизированная рука', 'Искусственные органы', 'Сделана для высокоточных манипуляций', '15000', 'робот_рука.jpg')
add_organ('Нейро-сердце', 'Искусственные органы', 'Стабильно работает при любых условиях', '8000', 'нейро_сердце.jpg')
add_organ('Индивидуальный глаз', 'Органы', 'Глаз, который подстраивается под любые условия освещения', '2000', 'инд_глаз.jpg')
add_organ('Генетический аппарат', 'Искусственные органы', 'Программист для твоего тела', '5000', 'генет_аппарат.jpg')
add_organ('Ноготь с Wi-Fi', 'Услуги', 'Можно подключиться к интернету в любое время', '300', 'ноготь_wifi.jpg')
add_organ('Сердце Супергероя', 'Органы', 'Энергия бьет ключом, подходит для спасения мира', '15000', 'сердце_супергероя.jpg')
add_organ('Ухо с усилением', 'Органы', 'Услышит даже шепот на расстоянии 5 км', '800', 'ухо_усиленное.jpg')
add_organ('Роботизированный мозг', 'Искусственные органы', 'Для улучшенной обработки информации', '10000', 'робо_мозг.jpg')
add_organ('Кожа с камуфляжем', 'Органы', 'Может адаптироваться к окружающей среде', '6000', 'кожа_камуфляж.jpg')
add_organ('Термометр желудка', 'Услуги', 'Учитывает температуру и метаболизм в реальном времени', '500', 'терм_желудка.jpg')
add_organ('Кибер-щупальца', 'Искусственные органы', 'Далеко простирающиеся возможности манипуляций', '12000', 'кибер_щупальца.jpg')
add_organ('Дыхание от марсианина', 'Органы', 'Может быть использовано на других планетах', '2500', 'дыхание_марсианина.jpg')
add_organ('Интерфейс для мыслей', 'Искусственные органы', 'С помощью этих имплантов ты сможешь общаться без слов', '8000', 'интерфейс_мыслей.jpg')
