import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QListWidget, QPushButton, QLineEdit,
    QInputDialog
)

# Интерфейс приложения
app = QApplication([])

window = QWidget()
window.setWindowTitle('Менеджер фильмов')
window.setMinimumSize(800, 600)

# Поле для ввода текста
text_field = QTextEdit()
text_field.setPlaceholderText("Введите описание фильма...")

# Список фильмов
list_films = QListWidget()
create_film = QPushButton('Добавить фильм')
delete_film = QPushButton('Удалить фильм')
save_film = QPushButton('Сохранить фильм')

# Список жанров
list_genres = QListWidget()
search_field = QLineEdit()
search_field.setPlaceholderText("Введите жанр фильма...")
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

# Размещение кнопок и списков
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

# Применение стилей
window.setStyleSheet("""
    QWidget {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f7f7f7;
        color: #333;
    }

    QTextEdit {
        border: 2px solid #00796b;
        border-radius: 12px;
        padding: 15px;
        background-color: #ffffff;
        font-size: 26px;
        color: #333;
        min-width: 400px;
        max-width: 600px;
    }

    QTextEdit::placeholder {
        color: #00796b;
    }

    QListWidget {
        border: 2px solid #00796b;
        background-color: #ffffff;
        border-radius: 10px;
        padding: 5px;
        color: #333;
        font-size: 20px;
    }

    QListWidget::item {
        border-radius: 5px;
    }

    QListWidget::item:hover {
        background-color: #00796b;
        color: white;
    }

    QLineEdit {
        border: 2px solid #00796b;
        border-radius: 12px;
        background-color: #ffffff;
        padding: 10px;
        font-size: 24px;
        color: #333;
        margin-bottom: 15px;
    }

    QLineEdit::placeholder {
        color: #00796b;
    }

    QPushButton {
        background-color: #00796b;
        color: white;
        border: none;
        padding: 12px 18px;
        font-size: 16px;
        border-radius: 10px;
        margin: 8px;
        min-width: 150px;
        text-align: center;
    }

    QPushButton:hover {
        background-color: #004d40;
    }

    QPushButton:pressed {
        background-color: #00332d;
    }

    QPushButton:focus {
        outline: none;
    }

    QPushButton[disabled="true"] {
        background-color: #757575;
    }

    QVBoxLayout, QHBoxLayout {
        spacing: 20px;
        margin: 25px;
    }

    QHBoxLayout > QWidget {
        margin-left: 15px;
        margin-right: 15px;
    }
                     
""")

# Функционал приложения
def show_info():
    film = list_films.selectedItems()[0].text()
    text_field.setText(films[film]['описание'])
    list_genres.clear()
    list_genres.addItems(films[film]['жанры'])

def film_create(): 
    film, input = QInputDialog.getText(window,'Добавить фильм','Название фильма:')
    if film != '' and film not in films:
        films[film] = {'описание':'', 'жанры':[]}
        list_films.addItem(film)

def film_save():
    if list_films.selectedItems():
        film = list_films.selectedItems()[0].text()
        films[film]['описание'] = text_field.toPlainText()

    file = open('films.json', 'w', encoding='utf-8')
    json.dump(films, file, ensure_ascii=False)

def film_delete():
    if list_films.selectedItems():
        film = list_films.selectedItems()[0].text()
        del films[film]
        list_films.clear()
        list_genres.clear()
        text_field.clear()
        list_films.addItems(films)
   
    file = open('films.json', 'w', encoding='utf-8')
    json.dump(films, file, ensure_ascii=False)

def genre_create():
    if list_films.selectedItems():
        film = list_films.selectedItems()[0].text()
        genre = search_field.text()
        if genre != '' and genre not in films[film]['жанры']:
            films[film]['жанры'].append(genre)
            list_genres.addItem(genre)
            search_field.clear()

def genre_delete():
    if list_genres.selectedItems():
        film = list_films.selectedItems()[0].text()
        genre = list_genres.selectedItems()[0].text()
        films[film]['жанры'].remove(genre)
        list_genres.clear()
        list_genres.addItems( films[film]['жанры'] )

    file = open('films.json', 'w', encoding='utf-8')
    json.dump(films, file, ensure_ascii=False)

def search():
    genre = search_field.text()
    if search_button.text() == 'Поиск по жанру':
        filtred_films = {}
        for film in films:
            if genre in films[film]['жанры']:
                filtred_films[film] = films[film]

        list_films.clear()
        list_films.addItems(filtred_films)
        search_button.setText('Сбросить поиск')
    elif search_button.text() == 'Сбросить поиск':
        search_field.clear()
        list_films.clear()
        list_films.addItems(films)
        search_button.setText('Поиск по жанру')

# Подключение обработки событий
list_films.itemClicked.connect(show_info) 
create_film.clicked.connect(film_create)
save_film.clicked.connect(film_save)
delete_film.clicked.connect(film_delete)
create_genre.clicked.connect(genre_create)
delete_genre.clicked.connect(genre_delete)
search_button.clicked.connect(search)


# Запуск приложения
file = open('films.json', encoding='utf-8')
films = json.load(file)

list_films.addItems(films)

window.show()
app.exec()
