from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QListWidget, QPushButton, QLineEdit
)

# Интерфейс приложения
app = QApplication([])
window = QWidget()

text_field = QTextEdit()

list_films = QListWidget()
create_film = QPushButton('Добавить фильм')
delete_film = QPushButton('Удалить фильм')
save_film = QPushButton('Сохранить фильм')

list_genres = QListWidget()
search_field = QLineEdit()
create_genre = QPushButton('Добавить жанр')
delete_genre = QPushButton('Удалить жанр')
search_button = QPushButton('Поиск по жанру')

# Расположение элементов интерфейса
main_line = QHBoxLayout()
lists_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()

main_line.addWidget(text_field)
main_line.addLayout(lists_line)

lists_line.addWidget(list_films)
h1_line.addWidget(create_film)
h1_line.addWidget(delete_film)
lists_line.addLayout(h1_line)
lists_line.addWidget(save_film)

lists_line.addWidget(list_genres)
lists_line.addWidget(search_field)
h2_line.addWidget(create_genre)
h2_line.addWidget(delete_genre)
lists_line.addLayout(h2_line)
lists_line.addWidget(search_button)

window.setLayout(main_line)

# Запуск приложения
window.show()
app.exec()
