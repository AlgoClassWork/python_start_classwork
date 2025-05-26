import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout, QListWidget,
    QPushButton, QVBoxLayout, QLineEdit, QInputDialog
)

# Создаем приложение
app = QApplication([])

window = QWidget()
window.resize(700, 500)
window.setWindowTitle("Менеджер Фильмов") 
window.setStyleSheet("""
    QWidget {
        background-color: lightgray; 
        font-size: 15px;
    }
    QTextEdit {
        background-color: white;
        color: black;
        border: 1px solid green;
        border-radius: 5px;
        padding: 5px;
    }
    QListWidget {
        background-color: white;
        color: black;
        border: 1px solid green;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton {
        background-color: #006b52; 
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 15px;
    }
    QPushButton:hover {
        background-color: #018c7c;
    }
    QLineEdit {
        background-color: white;
        color: black;
        border: 1px solid green;
        border-radius: 5px;
        padding: 5px;
    }
""")

# Создание элементов интерфейса
description_field = QTextEdit()
description_field.setPlaceholderText("Описание фильма...") 

films_list = QListWidget()
add_film_btn = QPushButton('Добавить фильм')
del_film_btn = QPushButton('Удалить фильм')
save_film_btn = QPushButton('Сохранить')

genres_list = QListWidget()
genre_field = QLineEdit()
genre_field.setPlaceholderText("Введите жанр...") 
add_genre_btn = QPushButton('Добавить жанр')
del_genre_btn = QPushButton('Удалить жанр')
search_genre_btn = QPushButton('Поиск по жанру')
# Размещение элементов интерфейса
main_line = QHBoxLayout()
lists_line = QVBoxLayout()
films_btns_line = QHBoxLayout()
genres_btns_line = QHBoxLayout()

main_line.addLayout(lists_line)

lists_line.addWidget(films_list)
lists_line.addLayout(films_btns_line)
films_btns_line.addWidget(add_film_btn)
films_btns_line.addWidget(del_film_btn)
lists_line.addWidget(save_film_btn)

lists_line.addWidget(genres_list)
lists_line.addWidget(genre_field)
lists_line.addLayout(genres_btns_line)
genres_btns_line.addWidget(add_genre_btn)
genres_btns_line.addWidget(del_genre_btn)
lists_line.addWidget(search_genre_btn)

main_line.addWidget(description_field)

window.setLayout(main_line)
# Функционал приложения
def database_writer():
    json.dump(films, open('films.json', 'w', encoding='utf-8'), ensure_ascii=False)

def show_film_info():
    film = films_list.selectedItems()[0].text()
    description_field.setText( films[film]['описание'] )
    genres_list.clear()
    genres_list.addItems(films[film]['жанры'])

def add_film():
    film = QInputDialog.getText(window, 'Добавить фильм', 'Название фильма:')[0]
    if film:
        films[film] = {'описание': '', 'жанры': []}
        films_list.addItem(film)
        database_writer()

def del_film():
    if films_list.selectedItems():
        film = films_list.selectedItems()[0].text()
        del films[film]
        films_list.clear()
        genres_list.clear()
        description_field.clear()
        films_list.addItems(films)
        database_writer()

def save_film():
    if films_list.selectedItems():
        film = films_list.selectedItems()[0].text()
        films[film]['описание'] = description_field.toPlainText()
        database_writer()

def add_genre():
    if films_list.selectedItems():
        film = films_list.selectedItems()[0].text()
        genre = genre_field.text()
        if genre not in films[film]['жанры']:
            films[film]['жанры'].append(genre)
            genres_list.addItem(genre)
            genre_field.clear()
            database_writer()

def del_genre():
    if films_list.selectedItems():
        film = films_list.selectedItems()[0].text()
        genre = genres_list.selectedItems()[0].text()
        films[film]['жанры'].remove(genre)
        genres_list.clear()
        genres_list.addItems( films[film]['жанры'] )
        database_writer()

def search_genre():
    if search_genre_btn.text() == 'Поиск по жанру':
        genre = genre_field.text()
        filtred_films = {}
        for film in films:
            if genre in films[film]['жанры']:
                filtred_films[film] = films[film]

        genre_field.clear()
        films_list.clear()
        films_list.addItems(filtred_films)

        search_genre_btn.setText('Сбросить')
    elif search_genre_btn.text() == 'Сбросить':
        films_list.clear()
        films_list.addItems(films)

        search_genre_btn.setText('Поиск по жанру')

# Подписки на события
films_list.itemClicked.connect(show_film_info)

add_film_btn.clicked.connect(add_film)
del_film_btn.clicked.connect(del_film)
save_film_btn.clicked.connect(save_film)

add_genre_btn.clicked.connect(add_genre)
del_genre_btn.clicked.connect(del_genre)
search_genre_btn.clicked.connect(search_genre)

# Запуск приложения
films = json.load( open('films.json', encoding='utf-8') )
films_list.addItems(films)

window.show()
app.exec()
