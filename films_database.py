from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout
)
# Создание интерфейса
app = QApplication([])
window = QWidget()

description_field = QTextEdit()

films_list = QListWidget()
add_film_btn = QPushButton('Добавить фильм')
del_film_btn = QPushButton('Удалить фильм')
update_description_btn = QPushButton('Обновить описание')

genres_list = QListWidget()
genre_field = QLineEdit()
add_genre_btn = QPushButton('Добавить жанр')
del_genre_btn = QPushButton('Удалить жанр')
search_film_btn = QPushButton('Поиск по жанру')

# Расположение элементов интерфейса
main_line = QHBoxLayout()

left_line = QVBoxLayout()
right_line = QVBoxLayout()

main_line.addLayout(left_line)
main_line.addLayout(right_line)

left_line.addWidget(description_field)

right_line.addWidget(films_list)
right_line.addWidget(add_film_btn)
right_line.addWidget(del_film_btn)
right_line.addWidget(update_description_btn)
right_line.addWidget(genres_list)
right_line.addWidget(genre_field)
right_line.addWidget(add_genre_btn)
right_line.addWidget(del_genre_btn)
right_line.addWidget(search_film_btn)

window.setLayout(main_line)
# Запуск приложения
window.show()
app.exec()
