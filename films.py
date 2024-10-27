import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QListWidget, QPushButton, QVBoxLayout, QLineEdit
)

# ИНТЕРФЕЙС
app = QApplication([])

window = QWidget()
window.setWindowTitle('Фильмы')
window.setStyleSheet("""
    QWidget { background-color: #f0f0f0; color: #333; font-family: Arial; }
    QTextEdit, QListWidget, QLineEdit {
        background-color: #fff; color: #333; border: 1px solid #ccc; border-radius: 5px; padding: 5px;
    }
    QPushButton {
        background-color: #007BFF; color: white; border: none; border-radius: 5px; padding: 10px;
        font-size: 14px;
    }
    QPushButton:hover { background-color: #0056b3; }
    QListWidget { margin-bottom: 10px; }
""")

text_field = QTextEdit()
list_films = QListWidget()
create_film = QPushButton('Добавить фильм')
delete_film = QPushButton('Удалить фильм')
save_film = QPushButton('Сохранить фильм')
list_genres = QListWidget()
search_field = QLineEdit()
search_field.setPlaceholderText('Введите жанр: ')
create_genre = QPushButton('Добавить жанр')
delete_genre = QPushButton('Удалить жанр')
search_button = QPushButton('Найти фильм по жанру')

# РАЗМЕЩЕНИЕ
main_line = QHBoxLayout()
main_line.addWidget(text_field)

list_line = QVBoxLayout()
main_line.addLayout(list_line)

list_line.addWidget(list_films)
h1_line = QHBoxLayout()
list_line.addLayout(h1_line)
h1_line.addWidget(create_film)
h1_line.addWidget(delete_film)
list_line.addWidget(save_film)

list_line.addWidget(list_genres)
list_line.addWidget(search_field)
h2_line = QHBoxLayout()
list_line.addLayout(h2_line)
h2_line.addWidget(create_genre)
h2_line.addWidget(delete_genre)
list_line.addWidget(search_button)

window.setLayout(main_line)
# ФУНКЦИОНАЛ
def show_film(): 
    name = list_films.selectedItems()[0].text()
    text_field.setText(films[name]['описание'])
    list_genres.clear()
    list_genres.addItems(films[name]['жанры'])
# СОБЫТИЯ
list_films.itemClicked.connect(show_film)
# ЗАПУСК
with open('data.json','r',encoding='utf-8') as file:
    films = json.load(file)

list_films.addItems(films)

window.resize(700, 500)
window.show()
app.exec()
