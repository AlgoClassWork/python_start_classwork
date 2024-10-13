from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout,
    QGroupBox, QRadioButton
)
from PyQt5.QtCore import Qt

# ИНТЕРФЕЙС
app = QApplication([])

# Установка стилей
app.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    QLabel {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    QGroupBox {
        font-size: 16px;
        font-weight: bold;
        margin: 10px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    QRadioButton {
        font-size: 14px;
        margin: 5px;
    }
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        cursor: pointer;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
""")

window = QWidget()
window.setWindowTitle('Memory card')

question_label = QLabel('Как переводится слово яблоко?')
answer_button = QPushButton('Ответить')

# форма вопроса
question_form = QGroupBox('Варианты ответов:')
rbtn1 = QRadioButton('dog')
rbtn2 = QRadioButton('cat')
rbtn3 = QRadioButton('apple')
rbtn4 = QRadioButton('father')

v_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
v_layout.addLayout(h1_layout)
v_layout.addLayout(h2_layout)
h1_layout.addWidget(rbtn1)
h1_layout.addWidget(rbtn2)
h2_layout.addWidget(rbtn3)
h2_layout.addWidget(rbtn4)
question_form.setLayout(v_layout)
# форма результата
result_form = QGroupBox('Результаты:')
result_label = QLabel('правильно')
answer_label = QLabel('apple')
layout = QVBoxLayout()
layout.addWidget(result_label)
layout.addWidget(answer_label)
result_form.setLayout(layout)
# РАЗМЕЩЕНИЕ
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(question_form)
main_layout.addWidget(result_form)
main_layout.addWidget(answer_button)
window.setLayout(main_layout)
# ФУНКЦИОНАЛ
def change_form():
    if answer_button.text() == 'Ответить':
        question_form.hide()
        result_form.show()
        answer_button.setText('Следующий вопрос')
    else:
        question_form.show()
        result_form.hide()
        answer_button.setText('Ответить')
# ПОДПИСКИ
answer_button.clicked.connect(change_form)
# ЗАПУСК
result_form.hide()
window.show()
app.exec()
