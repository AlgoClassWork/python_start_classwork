import os
import PyQt5

# Конфигурация PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(
    pyqt_path, "Qt5", "plugins", "platforms"
)

import json
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTextEdit,
    QListWidget,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
)


# === Инициализация приложения ===
app = QApplication([])
window = QWidget()
window.setWindowTitle("Кинопоиск")
window.setGeometry(100, 100, 1000, 600)


# === Элементы интерфейса ===
# Описание фильма
description_text = QTextEdit()

# Список и управление фильмами
films_list = QListWidget()
add_film_btn = QPushButton("Добавить фильм")
delete_film_btn = QPushButton("Удалить фильм")

# Список и управление жанрами
genres_list = QListWidget()
genre_input = QLineEdit()
genre_input.setPlaceholderText("Введите жанр...")
search_btn = QPushButton("Найти фильмы по жанру")
add_genre_btn = QPushButton("Добавить жанр")
delete_genre_btn = QPushButton("Удалить жанр")


# === Структура макета ===
main_layout = QHBoxLayout()
sidebar_layout = QVBoxLayout()

# Левая часть - описание
main_layout.addWidget(description_text, 1)

# Правая часть - списки и управление
main_layout.addLayout(sidebar_layout, 1)

# Фильмы
films_buttons_layout = QHBoxLayout()
sidebar_layout.addWidget(films_list)
sidebar_layout.addLayout(films_buttons_layout)
films_buttons_layout.addWidget(add_film_btn)
films_buttons_layout.addWidget(delete_film_btn)

# Жанры
genres_buttons_layout = QHBoxLayout()
sidebar_layout.addWidget(genres_list)
sidebar_layout.addWidget(genre_input)
sidebar_layout.addWidget(search_btn)
sidebar_layout.addLayout(genres_buttons_layout)
genres_buttons_layout.addWidget(add_genre_btn)
genres_buttons_layout.addWidget(delete_genre_btn)


# === Стили ===
stylesheet = """
    QWidget {
        background-color: #f5f5f5;
        color: #333;
    }
    
    QTextEdit, QListWidget, QLineEdit {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 5px;
        font-size: 11pt;
    }
    
    QPushButton {
        background-color: #007acc;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 8px;
        font-weight: bold;
    }
    
    QPushButton:hover {
        background-color: #005a9e;
    }
    
    QPushButton:pressed {
        background-color: #004578;
    }
"""

window.setStyleSheet(stylesheet)
window.setLayout(main_layout)


# == Функции для работы с фильмами и жанрами ===
def show_info():
    selected_film = films_list.currentItem().text()
    description_text.setText(films[selected_film]["описание"])
    genres_list.clear()
    genres_list.addItems(films[selected_film]["жанр"])

def save_info():
    if films_list.currentItem():
        selected_film = films_list.currentItem().text()
        films[selected_film]["описание"] = description_text.toPlainText()
        file = open('films.json', 'w', encoding='utf-8')
        json.dump(films, file, ensure_ascii=False, indent=4)

# Подписки на события
films_list.itemClicked.connect(show_info)
description_text.textChanged.connect(save_info)

# === Запуск приложения ===
file = open('films.json', 'r', encoding='utf-8')
films = json.load(file)
films_list.addItems(films)

window.show()
app.exec()
