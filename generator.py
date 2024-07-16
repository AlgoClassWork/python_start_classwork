from random import randint
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Генератор победителя!')
window.setStyleSheet("background-color: #e6e6e6;")  # Светло-серый фон окна

text = QLabel('Нажми чтобы узнать победителя')
text.setAlignment(Qt.AlignCenter)
text.setFont(QFont('Helvetica', 18))
text.setStyleSheet("color: #333;")  # Темно-серый цвет текста

result = QLabel(' ? ')
result.setAlignment(Qt.AlignCenter)
result.setFont(QFont('Helvetica', 48, QFont.Bold))
result.setStyleSheet("color: #2c3e50;")  # Темно-синий цвет текста

button = QPushButton('Сгенерировать')
button.setFont(QFont('Helvetica', 14))
button.setStyleSheet("""
    QPushButton {
        background-color: #3498db; 
        color: white; 
        border: 2px solid #2980b9; 
        border-radius: 10px; 
        padding: 10px 20px; 
        font-size: 16px; 
    }
    QPushButton:hover {
        background-color: #2980b9;
        border-color: #1f6f8b;
    }
    QPushButton:pressed {
        background-color: #1f6f8b;
        border-color: #1a3e5d;
    }
""")

#РАЗМЕЩЕНИЕ
layout = QVBoxLayout()

layout.addWidget(text)
layout.addWidget(result)
layout.addWidget(button)

window.setLayout(layout)

# ФУНКЦИОНАЛ
def show_result():
    text.setText('Победитель:')
    result.setText(str(randint(1, 100)))

# ПОДПИСКИ
button.clicked.connect(show_result)

# ЗАПУСК
window.show()
app.exec()
