from random import randint, shuffle
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton
)

style_sheet = """
QWidget {
    background-color: #e9ecef;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 16px;
    color: #343a40;
}

QLabel {
    font-weight: bold;
    margin-bottom: 10px;
}

QPushButton {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    font-weight: bold;
    transition: background-color 0.3s;
}

QPushButton:hover {
    background-color: #0056b3;
}

QGroupBox {
    background-color: #ffffff;
    border: 2px solid #ced4da;
    border-radius: 10px;
    margin-top: 20px;
    padding: 15px;
}

QRadioButton {
    margin: 5px;
    font-size: 14px;
}

QRadioButton::indicator {
    width: 25px;
    height: 25px;
}

QRadioButton::indicator:checked {
    background-color: #007bff;
    border: 2px solid #007bff;
}

QRadioButton::indicator:unchecked {
    background-color: #ffffff;
    border: 2px solid #ced4da;
}

QVBoxLayout, QHBoxLayout {
    spacing: 12px;
}

QLineEdit {
    border: 2px solid #ced4da;
    border-radius: 8px;
    padding: 10px;
}

QLineEdit:focus {
    border: 2px solid #007bff;
    background-color: #f8f9fa;
}
"""

class Question():
    def __init__(self,q,r,w1,w2,w3):
        self.question = q
        self.right = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

list_questions = [
    Question('Сколько дней в неделе?', '7', '5', '10', '14'),
    Question('Какой цвет у банана?', 'Желтый', 'Синий', 'Красный', 'Фиолетовый'),
    Question('Что тяжелее: килограмм ваты или килограмм железа?', 'Они одинаковые', 'Килограмм ваты', 'Килограмм железа', 'Ничто'),
    Question('Какой звук издает корова?', 'Му', 'Мяу', 'Гав', 'Угу'),
    Question('Сколько ушей у человека?', '2', '1', '3', '4'),
    Question('Какой месяц идет после января?', 'Февраль', 'Март', 'Декабрь', 'Август'),
    Question('Сколько колен у человека?', '2', '1', '3', '4'),
    Question('Какой океан самый большой?', 'Тихий', 'Атлантический', 'Индийский', 'Северный Ледовитый'),
    Question('Сколько букв в слове "кот"?', '3', '2', '4', '5'),
    Question('Какой из этих предметов не летает?', 'Стул', 'Птица', 'Самолет', 'Муха')
]

# Создание элементов интерфейса
app = QApplication([])
window = QWidget()
window.setStyleSheet(style_sheet)
question_label = QLabel('Сколько будет 2 + 2?')
answer_button = QPushButton('Ответить')

# Создание формы с вариантами ответов
answers_form = QGroupBox('Варианты ответов:')
rbtn1 = QRadioButton('пять')
rbtn2 = QRadioButton('один')
rbtn3 = QRadioButton('четыре')
rbtn4 = QRadioButton('не знаю')
v_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h1_line.addWidget(rbtn1)
h1_line.addWidget(rbtn2)
h2_line.addWidget(rbtn3)
h2_line.addWidget(rbtn4)
v_line.addLayout(h1_line)
v_line.addLayout(h2_line)
answers_form.setLayout(v_line)
# Создание формы с результатами
results_form = QGroupBox('Ваши результаты:')
result_label = QLabel('Правильно')
correct_label = QLabel('четыре')
line = QVBoxLayout()
line.addWidget(result_label)
line.addWidget(correct_label)
results_form.setLayout(line)
# Размещение элементов интерфейса
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answers_form)
main_layout.addWidget(results_form)
main_layout.addWidget(answer_button)
window.setLayout(main_layout)
# Функционал приложения
buttons = [rbtn1,rbtn2,rbtn3,rbtn4]

def render_question(q : Question):
    shuffle(buttons)
    question_label.setText(q.question)
    buttons[0].setText(q.right)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)

def check_answer():
    if buttons[0].isChecked():
        result_label.setText('Правильно!')
    else:
        result_label.setText('Не правильно :(')

def change_form():
    if answer_button.text() == 'Ответить':
        answers_form.hide()
        results_form.show()
        answer_button.setText('Следующий вопрос')
        check_answer()
    else:
        answers_form.show()
        results_form.hide()
        answer_button.setText('Ответить')
        render_question(list_questions[randint(0,len(list_questions) - 1)])

# Подписки на события
answer_button.clicked.connect(change_form)
# Запуск приложения
results_form.hide()
window.show()
app.exec()
