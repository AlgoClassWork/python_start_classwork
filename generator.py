from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Генератор победителя!')

text = QLabel('Нажми чтобы узнать победителя')
result = QLabel(' ? ')
button = QPushButton('Нажми на меня')
#РАЗМЕЩЕНИЕ
layout = QVBoxLayout()

layout.addWidget(text)
layout.addWidget(result)
layout.addWidget(button)

window.setLayout(layout)
# ЗАПУСК
window.show()
app.exec()
