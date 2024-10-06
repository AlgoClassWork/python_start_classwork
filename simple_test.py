from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton,
    QVBoxLayout, QHBoxLayout,
    QMessageBox
)
from PyQt5.QtCore import Qt

# ИНТЕРФЕЙС
app = QApplication([])

# Создание основного окна
window = QWidget()
window.setWindowTitle('Тест на слабоумие')
window.setFixedSize(400, 250)  # Фиксированный размер окна
window.setStyleSheet("background-color: #F0F0F0;")  # Фон окна

# Вопрос и кнопки
question = QLabel('Какого цвета чернокожие?')
question.setAlignment(Qt.AlignCenter)  # Центрирование текста
question.setStyleSheet("font-size: 18px; font-weight: bold; color: #333; margin: 20px;")

button_style = """
    QRadioButton {
        font-size: 16px;
        padding: 10px;
        margin: 5px;
        border: 2px solid #008CBA; /* Цвет рамки */
        border-radius: 10px; /* Закругление углов */
        background-color: #FFFFFF; /* Фоновый цвет */
    }
    QRadioButton::indicator {
        width: 25px;
        height: 25px;
    }
    QRadioButton::indicator:checked {
        background-color: #008CBA; /* Цвет выбранного индикатора */
        border-radius: 10px; /* Закругление углов */
    }
    QRadioButton::indicator:unchecked {
        background-color: #FFFFFF; /* Цвет невыбранного индикатора */
    }
    QRadioButton:hover {
        border: 2px solid #005F7F; /* Цвет рамки при наведении */
    }
"""
# Применение стиля к кнопкам
button1 = QRadioButton('белые')
button1.setStyleSheet(button_style)

button2 = QRadioButton('коричневые')
button2.setStyleSheet(button_style)

button3 = QRadioButton('голубые')
button3.setStyleSheet(button_style)

button4 = QRadioButton('серые')
button4.setStyleSheet(button_style)

# РАЗМЕЩЕНИЕ
layout = QVBoxLayout()

# Размещение вопроса
layout.addWidget(question)

# Размещение кнопок в горизонтальных линиях
top_h_layout = QHBoxLayout()
top_h_layout.addWidget(button1)
top_h_layout.addWidget(button2)

bot_h_layout = QHBoxLayout()
bot_h_layout.addWidget(button3)
bot_h_layout.addWidget(button4)

layout.addLayout(top_h_layout)
layout.addLayout(bot_h_layout)

# Установка основного макета окна
window.setLayout(layout)

# ФУНКЦИОНАЛ
def show_correct_message():
    msg_box = QMessageBox()
    msg_box.setText('Да ты гений!')
    msg_box.exec()

def show_incorrect_message():
    msg_box = QMessageBox()
    msg_box.setText('Твой ICQ -0')
    msg_box.exec()

# ПОДПИСКИ
button1.clicked.connect(show_incorrect_message)
button2.clicked.connect(show_correct_message)
button3.clicked.connect(show_incorrect_message)
button4.clicked.connect(show_incorrect_message)

# ЗАПУСК
window.show()
app.exec()
