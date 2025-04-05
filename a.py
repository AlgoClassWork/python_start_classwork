from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout)

class Question():
    def __init__(self, question, correct, w1, w2, w3):
        self.question = question
        self.correct = correct
        self.wrong1 = w1
        self.worng2 = w2
        self.wrong3 = w3

questions_list = [
    Question('На каком языке говорят в Бразилии?', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'),
    Question('Какая самая большая страна в мире по площади?', 'Россия', 'Канада', 'США', 'Китай'),
    Question('Кто написал роман "Преступление и наказание"?', 'Фёдор Достоевский', 'Лев Толстой', 'Антон Чехов', 'Александр Пушкин'),
    Question('Какая планета самая большая в Солнечной системе?', 'Юпитер', 'Сатурн', 'Земля', 'Марс'),
    Question('Какой элемент периодической таблицы имеет символ O?', 'Кислород', 'Азот', 'Углерод', 'Гелий'),
    Question('Как называется столица Японии?', 'Токио', 'Пекин', 'Сеул', 'Ханой'),
    Question('Сколько цветов в радуге?', '7', '6', '8', '9'),
    Question('Какой океан самый большой?', 'Тихий океан', 'Атлантический океан', 'Индийский океан', 'Северный Ледовитый океан'),
    Question('Кто является автором картины "Мона Лиза"?', 'Леонардо да Винчи', 'Пабло Пикассо', 'Винсент Ван Гог', 'Рембрандт'),
    Question('Что является символом Франции?', 'Эйфелева башня', 'Статуя Свободы', 'Колизей', 'Биг-Бен'),
]



# Создание приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')
window.show()
# Создание элементов интерфейса
question_label = QLabel('Как переводится apple?')
button = QPushButton('Ответить')
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
result_box = QGroupBox('Результат теста:')
result_label = QLabel('Правильно')
correct_label = QLabel('яблоко')

result_line = QVBoxLayout()
result_line.addWidget(result_label)
result_line.addWidget(correct_label, alignment=Qt.AlignHCenter)
result_box.setLayout(result_line)
# Размещение элементов интерфейса
main_line = QVBoxLayout()
main_line.addWidget(question_label, alignment=(Qt.AlignHCenter | Qt.AlignVCenter) )
main_line.addWidget(answer_box)
main_line.addWidget(result_box)
main_line.addWidget(button)
window.setLayout(main_line)
# Стилизация элементов интерфейса
window.setStyleSheet('background:white')
question_label.setStyleSheet('font-size:40px;color:red')
button.setStyleSheet('font-size:30px; padding:20px; background-color:lightgray')
answer_box.setStyleSheet('font-size:30px; padding:30px;')
result_box.setStyleSheet('font-size:30px; padding:30px;')
# Функционал приложения
buttons = [button1, button2, button3, button4]

def ask(question, right, wrong1, wrong2, wrong3):
    question_label.setText(question)
    shuffle(buttons)
    buttons[0].setText(right)
    buttons[1].setText(wrong1)
    buttons[2].setText(wrong2)
    buttons[3].setText(wrong3)
    correct_label.setText(right)

    answer_box.show()
    result_box.hide()

def check_answer():
    if buttons[0].isChecked():
        result_label.setText('Правильно!')
    else:
        result_label.setText('Неверно!')

    answer_box.hide()
    result_box.show()

button.clicked.connect(check_answer)
# Запуск приложения
ask('На каком языке говорят в Бразилии?','Португальский','Бразильский','Испанский','Итальянский')
app.exec()
