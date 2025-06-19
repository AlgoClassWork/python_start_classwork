from random import shuffle
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QVBoxLayout, QGroupBox, QRadioButton,
    QHBoxLayout, QPushButton
)

questions = [
    {'question': '2 + 2', 'correct': '4', 'wrong1': '5', 'wrong2': 'хз', 'wrong3': 'ыыы'},
    {'question': 'Столица Франции?', 'correct': 'Париж', 'wrong1': 'Берлин', 'wrong2': 'Лондон', 'wrong3': 'Рим'},
    {'question': 'Сколько дней в неделе?', 'correct': '7', 'wrong1': '5', 'wrong2': '10', 'wrong3': '8'},
    {'question': 'Цвет неба в ясный день?', 'correct': 'Синий', 'wrong1': 'Зелёный', 'wrong2': 'Красный', 'wrong3': 'Чёрный'},
    {'question': '5 * 5', 'correct': '25', 'wrong1': '20', 'wrong2': '15', 'wrong3': '30'},
    {'question': 'Сколько ног у паука?', 'correct': '8', 'wrong1': '6', 'wrong2': '10', 'wrong3': '4'},
    {'question': 'Какой металл самый лёгкий?', 'correct': 'Литий', 'wrong1': 'Железо', 'wrong2': 'Золото', 'wrong3': 'Медь'},
    {'question': 'Какой океан самый большой?', 'correct': 'Тихий', 'wrong1': 'Атлантический', 'wrong2': 'Индийский', 'wrong3': 'Северный Ледовитый'},
    {'question': 'Кто написал "Войну и мир"?', 'correct': 'Толстой', 'wrong1': 'Достоевский', 'wrong2': 'Пушкин', 'wrong3': 'Чехов'},
    {'question': 'Сколько будет 10 / 2?', 'correct': '5', 'wrong1': '2', 'wrong2': '10', 'wrong3': '0'},
]

# Стили приложения
style = """                 
    QWidget {
        background-color: white;
        font-family: sans-serif;
        padding: 10px
    }
    QLabel {
        font-size: 30px;
        font-weight: bold;
        qproperty-alignment: 'AlignCenter';
    }
    QGroupBox {
        border: none;
    }
    QRadioButton {
        font-size: 20px;
        spacing: 20px;
        margin-top: 20px;
    }
    QRadioButton::indicator {
        width: 20px;
        height: 20px;
        border-radius: 10px;
        border: 1px solid black;
        background: lightgray;
    }
    QRadioButton::indicator:checked {
        border: 1px solid yellow;
        background-color: yellow;
    }
    QPushButton {
        font-size: 20px;
        font-weight: bold;
        background-color: lightgray;
        border: none;
        border-radius: 10px;
        padding: 10px 50px;
        margin-top: 20px;
    }
    QPushButton:hover {
        background-color: yellow;
    }
                     
"""
# Создание виджетов приложения
app = QApplication([])

window = QWidget()
window.setWindowTitle('ТЕСТ НА ICQ')
window.resize(400, 250)

label_question = QLabel('Кто такой Шрек?')
button_submit = QPushButton('Ответить')

# Создание формы с ответами
group_answers = QGroupBox('')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

line_answers = QVBoxLayout()
line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
line_h1.addWidget(rbtn_1)
line_h1.addWidget(rbtn_2)
line_h2.addWidget(rbtn_3)
line_h2.addWidget(rbtn_4)
line_answers.addLayout(line_h1)
line_answers.addLayout(line_h2)
group_answers.setLayout(line_answers)

# Создание формы с результатом
group_result = QGroupBox('')
label_result = QLabel('Правильно')
label_correct = QLabel('___')

line_result = QVBoxLayout()
line_result.addWidget(label_result)
line_result.addWidget(label_correct)
group_result.setLayout(line_result)

# Размещение виджетов
line_main = QVBoxLayout()
line_main.addWidget(label_question)
line_main.addWidget(group_answers)
line_main.addWidget(group_result)
line_main.addWidget(button_submit)
window.setLayout(line_main)



# Функционал
current_question = 0
rbtns = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_question():
    group_answers.show()
    group_result.hide()
    button_submit.setText('Ответить')
    question_data = questions[ 5 ]
    label_question.setText(question_data['question'])
    shuffle(rbtns)
    rbtns[0].setText(question_data['correct'])
    rbtns[1].setText(question_data['wrong1'])
    rbtns[2].setText(question_data['wrong2'])
    rbtns[3].setText(question_data['wrong3'])

def show_result():
    group_answers.hide()
    group_result.show()
    button_submit.setText('Следующий вопрос')
    if rbtns[0].isChecked():
        label_result.setText('Правильно')
    else:
        label_result.setText('Не правильно')

def submit():
    if button_submit.text() == 'Ответить':
        show_result()
    else:
        show_question() 
# Подписки на события
button_submit.clicked.connect(submit)

# Запуск приложения
show_question()  
window.setStyleSheet(style)
window.show()
app.exec()
