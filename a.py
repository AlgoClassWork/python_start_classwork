from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout)
# Создание приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')
window.show()
# Создание элементов интерфейса
question = QLabel('Как переводится apple?')
button = QPushButton('ответить')
# Создание формы с вариантами ответов
answer_box = QGroupBox('Варианты ответов:')
button1 = QRadioButton('груша')
button2 = QRadioButton('яблоко')
button3 = QRadioButton('апельсин')
button4 = QRadioButton('банан')

answer_line = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h1.addWidget(button1)
h1.addWidget(button2)
h2.addWidget(button3)
h2.addWidget(button4)
answer_line.addLayout(h1)
answer_line.addLayout(h2)
answer_box.setLayout(answer_line)
# Создание формы с результатом
result_box = QGroupBox('Результат теста')
result_label = QLabel('Правильно')
correct_label = QLabel('яблоко')

result_line = QVBoxLayout()
result_line.addWidget(result_label)
result_line.addWidget(correct_label)
result_box.setLayout(result_line)
# Размещение элементов интерфейса
main_line = QVBoxLayout()
main_line.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter) )
main_line.addWidget(answer_box)
main_line.addWidget(result_box)
main_line.addWidget(button)
window.setLayout(main_line)
# Стилизация элементов интерфейса
window.setStyleSheet('background:white')
question.setStyleSheet('font-size:40px;color:red')
button.setStyleSheet('font-size:30px; padding:20px; background-color:lightgray')
answer_box.setStyleSheet('font-size:30px; padding:30px;')
# Запуск приложения
app.exec()
