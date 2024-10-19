from random import randint, shuffle
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

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [
    Question('Какой язык является самым распространенным в мире?', 'Китайский', 'Испанский', 'Английский', 'Русский'),
    Question('Какой из этих языков является романским?', 'Итальянский', 'Немецкий', 'Арабский', 'Японский'),
    Question('Какой язык изучается как второй наиболее часто?', 'Испанский', 'Французский', 'Китайский', 'Итальянский'),
    Question('Какой алфавит используется в русском языке?', 'Кириллица', 'Латиница', 'Греческий', 'Иероглифы'),
    Question('Какой язык является официальным в Бразилии?', 'Португальский', 'Испанский', 'Французский', 'Итальянский'),
    Question('На каком языке написана "Илиада"?', 'Древнегреческий', 'Латинский', 'Санскрит', 'Арабский'),
    Question('Какой язык имеет наибольшее количество говорящих в Европе?', 'Немецкий', 'Французский', 'Итальянский', 'Русский'),
    Question('Какой язык является официальным в Индии?', 'Хинди', 'Бенгальский', 'Панджаби', 'Тамильский'),
    Question('На каком языке говорится в Австралии как на родном?', 'Английский', 'Немецкий', 'Французский', 'Испанский'),
    Question('Какой из этих языков является искусственным?', 'Эсперанто', 'Немецкий', 'Японский', 'Китайский')
]


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
rbtns =  [rbtn1,rbtn2,rbtn3,rbtn4]
def ask(q : Question):
    shuffle(rbtns)
    question_label.setText(q.question)
    rbtns[0].setText(q.right_answer)
    rbtns[1].setText(q.wrong1)
    rbtns[2].setText(q.wrong2)
    rbtns[3].setText(q.wrong3)

def check_answer():
    a = 2
    question_form.hide()
    result_form.show()
    answer_button.setText('Следующий вопрос')

    if rbtns[0].isChecked():
        result_label.setText('Правильно!')
        window.correct += 1
    else:
        result_label.setText('Не правильно :(')

    correct_procent = int((window.correct / window.total) * 100)
    answer_label.setText(str(correct_procent) + '% ' + 'Правильных ответов')

def next_question():
    question_form.show()
    result_form.hide()
    answer_button.setText('Ответить')
    ask(questions_list[randint(0,len(questions_list) - 1)])

    window.total += 1
 
def change_form():
    if answer_button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

# ПОДПИСКИ
answer_button.clicked.connect(change_form)
# ЗАПУСК
window.total = 0
window.correct = 0
next_question()
result_form.hide()
window.show()
app.exec()
