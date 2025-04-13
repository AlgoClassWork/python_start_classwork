from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QListWidget, QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt

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
        font-size: 16px;
        color: #333;
        min-width: 400px;
        max-width: 600px;
    }

    QTextEdit::placeholder {
        color: #00796b;
    }

    QListWidget {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        color: #333;
        font-size: 14px;
        margin-bottom: 20px;
        min-width: 200px;
        max-width: 300px;
    }

    QListWidget::item {
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
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
        font-size: 14px;
        color: #333;
        margin-bottom: 15px;
        min-width: 200px;
        max-width: 300px;
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
        transition: background-color 0.3s, transform 0.3s;
    }

    QPushButton:hover {
        background-color: #004d40;
        transform: scale(1.05);
    }

    QPushButton:pressed {
        background-color: #00332d;
        transform: scale(0.98);
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

    /* Анимация для появления элементов */
    QWidget {
        animation: fadeIn 0.7s ease-out;
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
""")

# Подсказки
create_film.setToolTip("Нажмите, чтобы добавить новый фильм.")
delete_film.setToolTip("Нажмите, чтобы удалить выбранный фильм.")
save_film.setToolTip("Нажмите, чтобы сохранить изменения фильма.")
create_genre.setToolTip("Нажмите, чтобы добавить новый жанр.")
delete_genre.setToolTip("Нажмите, чтобы удалить выбранный жанр.")
search_button.setToolTip("Нажмите для поиска по жанру.")

# Запуск приложения
window.show()
app.exec()
