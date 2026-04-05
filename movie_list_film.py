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

movie_list = QListWidget()
movie_list.addItem('Фильм 1')
movie_list.addItem('Фильм 2')
movie_list.addItem('Фильм 3')
add_film_button = QPushButton('Добавить фильм')
delete_film_button = QPushButton('Удалить фильм')

genre_list = QListWidget()
genre_list.addItem('Жанр 1')
genre_list.addItem('Жанр 2')
genre_list.addItem('Жанр 3')
search_field = QLineEdit()
search_field.setPlaceholderText('Введите жанр для поиска...')

# Разметка интерфейса
main_layout = QHBoxLayout()
list_layout = QVBoxLayout()
list_buttons_layout = QHBoxLayout()

main_layout.addLayout(list_layout)
list_layout.addWidget(movie_list)
list_layout.addLayout(list_buttons_layout)
list_buttons_layout.addWidget(add_film_button)
list_buttons_layout.addWidget(delete_film_button)

list_layout.addWidget(genre_list)
list_layout.addWidget(search_field)

main_layout.addWidget(description_field)

window.setLayout(main_layout)

# Запуск
window.show()
app.exec()
