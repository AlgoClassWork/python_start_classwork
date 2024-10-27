{
    "Атака титанов" : {
        "описание": "Бла бла бла",
        "жанры": ["Фантастика","Ужасы"]
    },
    "Гурен Лагн" : {
        "описание": "Бу бу бу",
        "жанры": ["Фантастика","Комедия"]
    }
}


import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QListWidget, QPushButton, QVBoxLayout, QLineEdit
)

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('My Anime List')

# Стили
window.setStyleSheet("""
    QWidget {
        color: black;
    }
    QTextEdit {
        background-color: white;
        color: black;
        border: 1px solid #555;
        border-radius: 5px;
        padding: 5px;
    }
    QListWidget {
        background-color: white;
        border: 1px solid #555;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton {
        background-color: #0078d7;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px;
    }
    QPushButton:hover {
        background-color: #005a9e;
    }
    QLineEdit {
        background-color: white;
        color: black;
        border: 1px solid #555;
        border-radius: 5px;
        padding: 5px;
    }
""")

text_field = QTextEdit()


anime_list = QListWidget()
create_anime = QPushButton('Добавить аниме')
delete_anime = QPushButton('Удалить аниме')
save_anime = QPushButton('Сохранить изменения')

genre_list = QListWidget()
search_field = QLineEdit()
search_field.setPlaceholderText('Введите жанр: ')
create_genre = QPushButton('Добавить жанр')
delete_genre = QPushButton('Открепить жанр')
search_btn = QPushButton('Найти аниме по жанру')

# РАЗМЕЩЕНИЕ
main_layout = QHBoxLayout()
main_layout.addWidget(text_field)

list_layout = QVBoxLayout()
main_layout.addLayout(list_layout)

list_layout.addWidget(anime_list)
h1 = QHBoxLayout()
h1.addWidget(create_anime)
h1.addWidget(delete_anime)
list_layout.addLayout(h1)
list_layout.addWidget(save_anime)

list_layout.addWidget(genre_list)
list_layout.addWidget(search_field)
h2 = QHBoxLayout()
h2.addWidget(create_genre)
h2.addWidget(delete_genre)
list_layout.addLayout(h2)
list_layout.addWidget(search_btn)

window.setLayout(main_layout)
# ФУНКЦИОНАЛ
def anime_info():
    name = anime_list.selectedItems()[0].text()
    text_field.setText(anime_info[name]['описание'])

# СОБЫТИЯ
anime_list.itemClicked.connect(anime_info)
# ЗАПУСК
with open('data.json','r',encoding='utf-8') as file:
    anime_info = json.load(file)

anime_list.addItems(anime_info)

window.resize(700, 500)
window.show()
app.exec()
