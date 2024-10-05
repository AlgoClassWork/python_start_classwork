# pip install pyqt5
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
# ЭЛЕМЕНТЫ ИНТЕРФЕЙСА
app = QApplication([])
window = QWidget()
window.setWindowTitle('Генератор победителя')
text = QLabel('Нажми что бы узнать кто негр?')
button = QPushButton('Сгенерировать')
# СТИЛИЗАЦИЯ ЭЛЕМЕНТОВ
text.setStyleSheet('color:red ; font-size:30px')
button.setStyleSheet('background-color:lightgreen;font-size:30px')
# РАЗМЕЩЕНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА
line = QVBoxLayout()
line.addWidget(text)
line.addWidget(button)
window.setLayout(line)
# ФУНКЦИОНАЛ
def show_negr():
    names = ['Вася','Петя','Эльмир']
    name = names[random.randint(0,2)]
    text.setText('Негр по имени: ' + name)
# ПОДПИСКИ НА СОБЫТИЯ
button.clicked.connect(show_negr)
# ЗАПУСК
window.show()
app.exec()

