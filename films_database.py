import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QListWidget, QLineEdit, QTextEdit, QInputDialog,
    QHBoxLayout, QVBoxLayout
)

# Создание интерфейса
app = QApplication([])
window = QWidget()
window.resize(800,500)
window.setWindowTitle('Кинопоиск')


description_field = QTextEdit()
description_field.setPlaceholderText('Введите описание')

films_list = QListWidget()
add_film_btn = QPushButton('Добавить фильм')
del_film_btn = QPushButton('Удалить фильм')
update_description_btn = QPushButton('Обновить описание')

genres_list = QListWidget()
genre_field = QLineEdit()
genre_field.setPlaceholderText('Введите жанр')
add_genre_btn = QPushButton('Добавить жанр')
del_genre_btn = QPushButton('Удалить жанр')
search_film_btn = QPushButton('Поиск по жанру')

# Расположение элементов интерфейса
main_line = QHBoxLayout()

left_line = QVBoxLayout()
right_line = QVBoxLayout()

films_btn_line = QHBoxLayout()
genres_btn_line = QHBoxLayout()

main_line.addLayout(left_line)
main_line.addLayout(right_line)

left_line.addWidget(description_field)

right_line.addWidget(films_list)
right_line.addLayout(films_btn_line)
films_btn_line.addWidget(add_film_btn)
films_btn_line.addWidget(del_film_btn)
right_line.addWidget(update_description_btn)
right_line.addWidget(genres_list)
right_line.addWidget(genre_field)
right_line.addLayout(genres_btn_line)
genres_btn_line.addWidget(add_genre_btn)
genres_btn_line.addWidget(del_genre_btn)
right_line.addWidget(search_film_btn)

window.setLayout(main_line)

# Фукнционал приложения
def update_db():
    file = open('films.json', 'w', encoding='utf-8') 
    json.dump(films, file, ensure_ascii=False)

def show_film():
    film = films_list.selectedItems()[0].text() 
    description_field.setText(films[film]['описание'])
    genres_list.clear()
    genres_list.addItems(films[film]['жанры'])

def add_film():
    film, ok = QInputDialog().getText(window, 'Добавить фильм', 'Название фильма:')
    if film and ok:
        films_list.addItem( film )
        films[ film ] = { 'описание' : '','жанры': []  }
        update_db()

def del_film():
    if films_list.selectedItems():
        film = films_list.selectedItems()[0].text() 
        del films[film]
        films_list.clear()
        genres_list.clear()
        description_field.clear()
        films_list.addItems(films)
        update_db()

def update_description():
    if films_list.selectedItems():
        film = films_list.selectedItems()[0].text()
        films[film]['описание'] = description_field.toPlainText()
        update_db()

def add_genre():
    if films_list.selectedItems():
        film = films_list.selectedItems()[0].text()
        genre = genre_field.text()
        if genre:
            films[film]['жанры'].append(genre)
            genres_list.addItem(genre)
            genre_field.clear()
            update_db()

def del_genre():
    if films_list.selectedItems() and genres_list.selectedItems():
        film = films_list.selectedItems()[0].text()
        genre = genres_list.selectedItems()[0].text()
        films[film]['жанры'].remove(genre)
        genres_list.clear()
        genres_list.addItems(films[film]['жанры'])
        update_db()

def search_film():
    genre = genre_field.text()
    if search_film_btn.text() == 'Поиск по жанру' and genre:
        filtred_films = {}
        for film in films:
            if genre in films[film]['жанры']:
                filtred_films[film] = films[film]

        films_list.clear()
        genres_list.clear()
        genre_field.clear()
        films_list.addItems(filtred_films)
        search_film_btn.setText('Сбросить')
    else:
        films_list.clear()
        genres_list.clear()
        genre_field.clear()
        films_list.addItems(films)
        search_film_btn.setText('Поиск по жанру')

# Подписки на события
films_list.itemClicked.connect( show_film )
add_film_btn.clicked.connect( add_film )
del_film_btn.clicked.connect( del_film )
update_description_btn.clicked.connect( update_description )
add_genre_btn.clicked.connect(add_genre)
del_genre_btn.clicked.connect(del_genre)
search_film_btn.clicked.connect(search_film)


# Стилизация приложения
app.setStyleSheet("""
    QWidget {
        background-color: #f7f7f7;
        color: #2e2e2e;
        font-family: 'Segoe UI', 'Roboto', sans-serif;
        font-size: 16px;
    }

    QTextEdit, QListWidget, QLineEdit {
        background-color: #ffffff;
        border: 1px solid #dcdcdc;
        border-radius: 6px;
        padding: 6px;
    }

    QTextEdit:focus, QListWidget:focus, QLineEdit:focus {
        border: 1px solid #6c63ff;
    }

    QPushButton {
        background-color: #6c63ff;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 6px 12px;
        font-weight: 500;
    }

    QPushButton:hover {
        background-color: #5a54e3;
    }

    QPushButton:pressed {
        background-color: #4e49c7;
    }

    QPushButton#search_film_btn {
        background-color: #00bfa5;
    }

    QPushButton#search_film_btn:hover {
        background-color: #00a48e;
    }

    QPushButton#search_film_btn:pressed {
        background-color: #008c78;
    }

    QListWidget {
        border: 1px solid #dcdcdc;
        border-radius: 6px;
    }

    QListWidget::item:selected {
        background-color: #6c63ff;
        color: white;
        border-radius: 4px;
    }

    QScrollBar:vertical {
        background: transparent;
        width: 8px;
        margin: 2px;
    }

    QScrollBar::handle:vertical {
        background: #cccccc;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical:hover {
        background: #b3b3b3;
    }
""")

# Запуск приложения
file = open('films.json', 'r', encoding='utf-8') 
films = json.load(file)

films_list.addItems(films)

window.show()
app.exec()
