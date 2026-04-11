import os
import PyQt5

# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")


from PyQt5.QtWidgets import (
     QApplication, QWidget, QTextEdit, QListWidget, QPushButton, QLineEdit,
     QHBoxLayout, QVBoxLayout
)

# Создание интерфейса
app = QApplication([])
window = QWidget()
window.setWindowTitle('Мой список фильмов')
window.resize(800, 600)

description_field = QTextEdit() 
description_field.setPlaceholderText('Введите описание фильма...')

film_list = QListWidget()
add_film_button = QPushButton('Добавить фильм')
delete_film_button = QPushButton('Удалить фильм')

genre_list = QListWidget()
search_field = QLineEdit()
search_field.setPlaceholderText('Введите жанр для поиска...')
add_genre_button = QPushButton('Добавить жанр')
delete_genre_button = QPushButton('Удалить жанр')
search_button = QPushButton('Поиск')

# Разметка интерфейса
main_layout = QHBoxLayout()
list_layout = QVBoxLayout()
list_buttons_layout = QHBoxLayout()
list_buttons_layout2 = QHBoxLayout()

main_layout.addLayout(list_layout)

list_layout.addWidget(film_list)
list_layout.addLayout(list_buttons_layout)
list_buttons_layout.addWidget(add_film_button)
list_buttons_layout.addWidget(delete_film_button)

list_layout.addWidget(genre_list)
list_layout.addWidget(search_field)
list_layout.addLayout(list_buttons_layout2)
list_buttons_layout2.addWidget(add_genre_button)
list_buttons_layout2.addWidget(delete_genre_button)
list_layout.addWidget(search_button)

main_layout.addWidget(description_field)

window.setLayout(main_layout)

# Функционал приложения

# Подписки на события

# Запуск

window.show()
app.exec()
