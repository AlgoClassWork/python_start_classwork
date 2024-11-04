import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout, QListWidget,
    QPushButton, QVBoxLayout, QLineEdit
)

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Сериалы')

# Создание виджетов
review_field = QTextEdit()
serial_list = QListWidget()
create_serial = QPushButton('Добавить сериал')
delete_serial = QPushButton('Удалить сериал')
save_changes = QPushButton('Сохранить изменения')

genre_list = QListWidget()
search_field = QLineEdit()
search_field.setPlaceholderText('Введите жанр:')
create_genre = QPushButton('Добавить жанр')
delete_genre = QPushButton('Открепить жанр')
search_button = QPushButton('Поиск по жанру')

# РАЗМЕЩЕНИЕ
main_line = QHBoxLayout()
list_line = QVBoxLayout()
main_line.addWidget(review_field)
main_line.addLayout(list_line)

list_line.addWidget(serial_list)
h1 = QHBoxLayout()
list_line.addLayout(h1)
h1.addWidget(create_serial)
h1.addWidget(delete_serial)
list_line.addWidget(save_changes)

list_line.addWidget(genre_list)
list_line.addWidget(search_field)
h2 = QHBoxLayout()
list_line.addLayout(h2)
h2.addWidget(create_genre)
h2.addWidget(delete_genre)
list_line.addWidget(search_button)

window.setLayout(main_line)

# СТИЛИЗАЦИЯ
window.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    QTextEdit {
        border: 1px solid #cccccc;
        border-radius: 5px;
        padding: 10px;
        background-color: #ffffff;
        font-size: 20px;
    }
    QListWidget {
        border: 1px solid #cccccc;
        border-radius: 5px;
        background-color: #ffffff;
    }
    QPushButton {
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 15px;
        margin: 5px;
        font-size: 15px;
    }
    QPushButton:hover {
        background-color: #0056b3;
    }
    QLineEdit {
        border: 1px solid #cccccc;
        border-radius: 5px;
        padding: 5px;
    }
""")

# ЗАПУСК
file = open('database.json','r', encoding='utf-8')
serials = json.load(file)
serial_list.addItems(serials)

window.resize(700, 500)
window.show()
app.exec()
