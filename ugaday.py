#pip install PyQt5
from PyQt5.QtWidgets import (QApplication, QWidget,
QLabel, QLineEdit, QPushButton, QVBoxLayout)
# Создание приложения и экрана
app = QApplication([])
window = QWidget()
window.setWindowTitle('Угадай число')
# Создание виджетов (элементы интерфейса)
game_label = QLabel('Игра угадай число')
text_input = QLineEdit()
text_input.setPlaceholderText('Введите число')
button = QPushButton('Нажми на меня')
# Размещение виджетов
line = QVBoxLayout()
line.addWidget(game_label)
line.addWidget(text_input)
line.addWidget(button)
window.setLayout(line)
# Запуск приложения
window.show()
app.exec()
