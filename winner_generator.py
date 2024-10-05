# pip install pyqt5
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
# ЭЛЕМЕНТЫ ИНТЕРФЕЙСА
app = QApplication([])
window = QWidget()
window.setWindowTitle('Генератор победителя')

text = QLabel('Нажми что бы узнать кто негр?')
text.setStyleSheet('color:red ; font-size:30px')
button = QPushButton('Сгенерировать')
button.setStyleSheet('background-color:lightgreen;font-size:30px')
# РАЗМЕЩЕНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА
line = QVBoxLayout()
line.addWidget(text)
line.addWidget(button)
window.setLayout(line)

window.show()
app.exec()

