from random import randint
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QVBoxLayout, QLineEdit, QPushButton)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Угадай число')  # Добавляем заголовок окна

text_label = QLabel('Я загадал число от 1 до 100')
input_field = QLineEdit()
result_btn = QPushButton('Ответить')

# Создаем стилизацию через CSS
style = """
    QWidget {
        font-size: 16px;
    }
    QLabel {
        font-size: 18px;
        margin-bottom: 10px;
    }
    QLineEdit {
        padding: 8px;
        font-size: 16px;
        border: 2px solid #ccc;
        border-radius: 4px;
    }
    QPushButton {
        padding: 10px 20px;
        font-size: 16px;
        background-color: #4CAF50; /* зеленый */
        color: white;
        border: none;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #45a049; /* темно-зеленый */
    }
"""

window.setStyleSheet(style)

main_layout = QVBoxLayout()
main_layout.addWidget(text_label)
main_layout.addWidget(input_field)
main_layout.addWidget(result_btn)
window.setLayout(main_layout)

win_num = randint(1, 100)

def show_result():
    your_num = int(input_field.text())
    if your_num > win_num:
        text_label.setText('Загаданное число меньше')
    elif your_num < win_num:
        text_label.setText('Загаданное число больше')
    else:
        text_label.setText('Вы победили')

result_btn.clicked.connect(show_result)

window.show()
app.exec()
