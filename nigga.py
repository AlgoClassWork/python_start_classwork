from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout)

#создание виджетов
app = QApplication([])
window = QWidget()

text = QLabel('Узнай кто нигга!')
button = QPushButton('Нажми на меня')

#размещение
line = QVBoxLayout()
line.addWidget(text)
line.addWidget(button)

window.setLayout(line)
#запуск приложения
window.show()
app.exec()
