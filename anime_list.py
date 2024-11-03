import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QListWidget, QPushButton, QVBoxLayout, QLineEdit, QInputDialog
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
    genre_list.clear()
    genre_list.addItems(anime_info[name]['жанры'])

def add_anime():
   name, ok = QInputDialog().getText(window,'Добавить','Название:')
   if name != '':
      anime_info[name] = {'описание':'','жанры':[]}
      anime_list.addItem(name)
      with open('data.json', 'w', encoding='utf-8') as file:
         json.dump(anime_info, file, ensure_ascii=False)

def del_anime():
   if anime_list.selectedItems():
      name = anime_list.selectedItems()[0].text()
      del anime_info[name]
      anime_list.clear()
      genre_list.clear()
      text_field.clear()
      anime_list.addItems(anime_info)
      with open('data.json', 'w', encoding='utf-8') as file:
         json.dump(anime_info, file, ensure_ascii=False)

def save_changes():
   if anime_list.selectedItems():
      name = anime_list.selectedItems()[0].text()
      anime_info[name]['описание'] = text_field.toPlainText()
      with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(anime_info, file, ensure_ascii=False)

def add_genre():
   if anime_list.selectedItems():
      name = anime_list.selectedItems()[0].text() 
      genre = search_field.text() 
      if genre != '' and genre not in anime_info[name]['жанры']:
        anime_info[name]['жанры'].append(genre)
        genre_list.addItem(genre)
        search_field.clear()
        with open('data.json', 'w', encoding='utf-8') as file:
                json.dump(anime_info, file, ensure_ascii=False)

# СОБЫТИЯ
anime_list.itemClicked.connect(anime_info)
create_anime.clicked.connect(add_anime)
delete_anime.clicked.connect(del_anime)
save_anime.clicked.connect(save_changes)
create_genre.clicked.connect(add_genre)
# ЗАПУСК
with open('data.json','r',encoding='utf-8') as file:
    anime_info = json.load(file)

anime_list.addItems(anime_info)

window.resize(700, 500)
window.show()
app.exec()
