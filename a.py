from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)

class Question:
    def __init__(self, question, correct, wrong1, wrong2, wrong3):
        self.question = question
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [
    Question('Какой звук издает молчание?', 'тишина', 'громко', 'музыка', 'тихо'),
    Question('Сколько весит невидимый щенок?', 'ничего', '1 кг', '5 кг', 'чуть-чуть'),
    Question('Какой цвет у воздуха?', 'прозрачный', 'синий', 'зеленый', 'желтый'),
    Question('Сколько глаз у трехголового дракона?', '6', '3', '9', '12'),
    Question('В каком месяце 28 дней?', 'февраль', 'все', 'апрель', 'январь'),
    Question('Какой вкус у дыма?', 'ничего', 'сладкий', 'горький', 'кислый'),
    Question('Сколько ног у единорога?', '4', '3', '5', '6'),
    Question('Какого цвета тень?', 'черная', 'белая', 'цветная', 'прозрачная'),
    Question('Что происходит, когда идет дождь из конфет?', 'вкусно', 'влажно', 'солнечно', 'невозможно'),
    Question('Какой вес у мысли?', 'неизмеримая', 'легкая', 'тяжелая', 'весит столько, сколько надо'),
]

app = QApplication([])

# Установка стилей
style_sheet = """
    QWidget {
        font-family: Arial, sans-serif;
        font-size: 18px;
        color: #343a40;
    }
    QGroupBox {
        font-weight: bold;
        margin: 20px;
        border: 2px solid #6c757d;
        border-radius: 10px;
        background-color: #ffffff;
        padding: 15px;
    }
    QRadioButton {
        margin: 10px;
        font-size: 18px;
    }
    QPushButton {
        background-color: #007bff;
        color: white;
        padding: 15px;
        border: none;
        border-radius: 10px;
        font-size: 20px;
    }
    QPushButton:hover {
        background-color: #0056b3;
    }
    QLabel {
        font-size: 30px;
    }
"""

# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
lb_Question.setWordWrap(True)

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# Размещаем все виджеты в окне
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(20)  

# Создаем главное окно
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.resize(700, 500)  
window.setStyleSheet(style_sheet)  
# Функционал
buttons = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q : Question):
    shuffle(buttons)
    lb_Question.setText(q.question)
    buttons[0].setText(q.correct)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)

def check_answer():
    if buttons[0].isChecked():
        window.correct += 1
        lb_Result.setText('Правильно!')
    else:
        lb_Result.setText('Не правильно :(')

    result = str(int(window.correct/window.total * 100))
    lb_Correct.setText(result + '% Правильных ответов')

def next_question():
    window.total += 1
    shuffle(questions_list)
    ask(questions_list[0])

def change_form():
    if btn_OK.text() == 'Ответить':
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Следующий вопрос')
        check_answer()
    else:
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_OK.setText('Ответить')
        next_question()

# Подписки на событиия
btn_OK.clicked.connect(change_form)
# Запуск
window.total = 0
window.correct = 0
next_question()
AnsGroupBox.hide()
window.show()
app.exec()
