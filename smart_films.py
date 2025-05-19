from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout, QListWidget,
    QPushButton, QVBoxLayout, QLineEdit, QLabel
)
from PyQt5.QtCore import Qt

# Создаем приложение
app = QApplication([])

# --- Настройка основного окна ---
window = QWidget()
window.setWindowTitle("Менеджер Фильмов")
window.setStyleSheet("""
    QWidget {
        background-color: #F5F5F5; /* Светло-серый фон */
        color: #333; /* Темно-серый текст */
        font-size: 14px;
    }
""")

# --- Создание элементов интерфейса ---
# Блок описания фильма
description_label = QLabel("Описание фильма:")
description_field = QTextEdit()
description_field.setPlaceholderText("Введите описание фильма...")
description_field.setStyleSheet("""
    QTextEdit {
        background-color: #FFF;
        color: #333;
        border: 1px solid #DDD;
        border-radius: 5px;
        padding: 8px;
    }
""")

# Блок списка фильмов и кнопок управления
films_label = QLabel("Фильмы:")
films_list = QListWidget()
films_list.addItems(["Интерстеллар", "Начало", "Драйв"])
films_list.setStyleSheet("""
    QListWidget {
        background-color: #FFF;
        color: #333;
        border: 1px solid #DDD;
        border-radius: 5px;
        padding: 8px;
        min-height: 150px; /* Зададим минимальную высоту для списка */
    }
    QListWidget::item:selected {
        background-color: #E0F2F7; /* Цвет выделения */
        color: #2196F3;
    }
""")
add_film_btn = QPushButton('Добавить')
del_film_btn = QPushButton('Удалить')
films_btns_layout = QHBoxLayout()
films_btns_layout.addWidget(add_film_btn)
films_btns_layout.addWidget(del_film_btn)

save_film_btn = QPushButton('Сохранить описание')
save_film_btn.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50; /* Зеленый цвет для сохранения */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 15px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #43A047;
    }
""")

films_layout = QVBoxLayout()
films_layout.addWidget(films_label)
films_layout.addWidget(films_list)
films_layout.addLayout(films_btns_layout)
films_layout.addWidget(save_film_btn)

# Блок списка жанров и поиска
genres_label = QLabel("Жанры:")
genres_list = QListWidget()
genres_list.addItems(["Фантастика", "Драма", "Триллер"])
genres_list.setStyleSheet(films_list.styleSheet()) # Используем стиль как у списка фильмов
genre_field = QLineEdit()
genre_field.setPlaceholderText("Введите жанр для поиска...")
genre_field.setStyleSheet("""
    QLineEdit {
        background-color: #FFF;
        color: #333;
        border: 1px solid #DDD;
        border-radius: 5px;
        padding: 8px;
        min-width: 150px; /* Зададим минимальную ширину для поля ввода */
    }
""")
add_genre_btn = QPushButton('Добавить')
del_genre_btn = QPushButton('Удалить')
search_genre_btn = QPushButton('Поиск')
search_genre_btn.setStyleSheet("""
    QPushButton {
        background-color: #2196F3; /* Синий цвет для поиска */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 15px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #1E88E5;
    }
""")
genres_btns_layout = QHBoxLayout()
genres_btns_layout.addWidget(add_genre_btn)
genres_btns_layout.addWidget(del_genre_btn)
genres_btns_layout.addWidget(search_genre_btn)

genres_layout = QVBoxLayout()
genres_layout.addWidget(genres_label)
genres_layout.addWidget(genres_list)
genres_layout.addWidget(genre_field)
genres_layout.addLayout(genres_btns_layout)

# --- Размещение элементов интерфейса ---
main_layout = QHBoxLayout()

# Левая часть - списки и кнопки
left_layout = QVBoxLayout()
left_layout.addLayout(films_layout)
left_layout.addLayout(genres_layout)
main_layout.addLayout(left_layout)

# Правая часть - описание фильма
right_layout = QVBoxLayout()
right_layout.addWidget(description_label)
right_layout.addWidget(description_field)
main_layout.addLayout(right_layout, 1) # Вес 1, чтобы занимало больше места

window.setLayout(main_layout)

# --- Запуск приложения ---
window.show()
app.exec()
