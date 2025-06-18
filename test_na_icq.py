from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QVBoxLayout, QGroupBox, QRadioButton,
    QHBoxLayout, QPushButton
)
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
def show_question(question, ans1, ans2, ans3, ans4):
    group_answers.show()
    group_result.hide()
    button_submit.setText('Ответить')
    label_question.setText(question)
    rbtn_1.setText(ans1)
    rbtn_2.setText(ans2)
    rbtn_3.setText(ans3)
    rbtn_4.setText(ans4)

def show_result():
    group_answers.hide()
    group_result.show()
    button_submit.setText('Следующий вопрос')
    if rbtn_2.isChecked():
        label_result.setText('Правильно')
    else:
        label_result.setText('Не правильно')

def submit():
    if button_submit.text() == 'Ответить':
        show_result()
    else:
        show_question(question='2 + 2', ans1='5', ans2='4', ans3='Хз', ans4='ыыы') 
# Подписки на события
button_submit.clicked.connect(submit)

# Запуск приложения
show_question(question='2 + 2', ans1='5', ans2='4', ans3='Хз', ans4='ыыы')  
window.setStyleSheet(style)
window.show()
app.exec()
