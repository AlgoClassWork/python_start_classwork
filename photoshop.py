from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLabel)
from PyQt5.QtCore import Qt # Импортируем Qt для выравнивания

# Интерфейс приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('Фотошоп на минималках')
window.resize(800,400)

# Устанавливаем общий стиль для всего приложения в светлых тонах
window.setStyleSheet("""
    QWidget {
        background-color: lightgray; /* Очень светло-серый фон */
        color: black; /* Темный текст для контраста */
        font-family: 'Segoe UI', sans-serif;
        font-size: 15px;
    }
    QPushButton {
        background-color: lightblue; /* Светло-серый фон кнопок */
        border: 1px solid black; /* Более светлая рамка */
        border-radius: 5px; /* Скругленные углы */
        padding: 10px 15px; /* Отступы внутри кнопки */
        color: black; /* Темный текст кнопок */
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: blue; /* Чуть темнее при наведении */
    }
    QListWidget {
        background-color: white; /* Белый фон списка */
        border: 1px solid black; /* Светлая рамка */
        border-radius: 5px;
        padding: 5px;
        color: black; /* Темный текст списка */
    }
    QListWidget::item {
        padding: 5px;
    }
    QListWidget::item:selected {
        background-color: lightblue; /* Светло-голубой фон для выбранных элементов */
        color: black;
    }
    QLabel {
        color: black; /* Темный текст для меток */
    }
    #image_lbl { /* Стиль для конкретного QLabel с objectName 'image_lbl' */
        background-color: white; /* Очень светлый фон для области изображения */
        border: 1px solid black; /* Светлая пунктирная рамка */
        qproperty-alignment: AlignCenter; /* Выравнивание содержимого по центру */
        font-weight: bold;
    }
""")


folder_btn = QPushButton('Папка')
files_list = QListWidget()

image_lbl = QLabel('Картинка')
image_lbl.setObjectName('image_lbl') # Присваиваем objectName для стилизации

left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
flip_btn = QPushButton('Зеркало')
sharpen_btn = QPushButton('Резкость')
gray_btn = QPushButton('Ч/Б')

# Размещение
main_line = QHBoxLayout()
v1_line = QVBoxLayout()
v2_line = QVBoxLayout()
btns_line = QHBoxLayout()

v1_line.addWidget(folder_btn)
v1_line.addWidget(files_list)
v2_line.addWidget(image_lbl)

btns_line.addWidget(left_btn)
btns_line.addWidget(right_btn)
btns_line.addWidget(flip_btn)
btns_line.addWidget(sharpen_btn)
btns_line.addWidget(gray_btn)

main_line.addLayout(v1_line, 30)
main_line.addLayout(v2_line, 70)
v2_line.addLayout(btns_line)

window.setLayout(main_line)

# Запуск приложения
window.show()
app.exec()
