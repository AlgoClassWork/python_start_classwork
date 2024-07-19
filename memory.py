from random import shuffle
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton, QPushButton,
    QGroupBox, QVBoxLayout)

class Question():
    def __init__(self,q,r,w1,w2,w3):
        self.question = q
        self.right_ans = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

questions = [
    Question('Почему носороги такие большие и сильные?', 'Чтобы защищаться от хищников', 'Не знаю', 'Для спортивных соревнований', 'Потому что они едят много капусты'),
    Question('Зачем у павлинов такие красивые хвосты?', 'Чтобы завоевать партнёршу', 'Мне всё равно', 'Для защиты от дождя', 'Это их секретная защита'),
    Question('Почему у медведей так много шерсти?', 'Чтобы не мёрзнуть зимой', 'Это загадка', 'Для моды', 'Потому что они любят покрываться шелком'),
    Question('Зачем у жирафов такие длинные шеи?', 'Чтобы достать листья на вершинах деревьев', 'Не знаю', 'Для прыжков высоко', 'Это результат стрейчинга'),
    Question('Почему у бабочек такие яркие крылья?', 'Чтобы отпугивать хищников', 'Мне всё равно', 'Для танцев', 'Это нарядные плащи'),
    Question('Зачем пчёлы собирают пыльцу?', 'Для производства мёда и кормления личинок', 'Не интересно', 'Для обогащения почвы', 'Это их хобби и занятие на выходные'),
    Question('Почему кенгуру прыгают?', 'Чтобы передвигаться быстро по просторам Австралии', 'Это загадка', 'Для забавы', 'Потому что у них пружинки в ногах'),
    Question('Зачем у львов такая громкая маненя?', 'Для общения с семьёй и отпугивания конкурентов', 'Мне неинтересно', 'Для попытки выделения', 'Это их способ зова врагов'),
    Question('Почему у слонов такие длинные бивни?', 'Чтобы защищаться и копать корни', 'Не знаю', 'Для сувениров', 'Это след от огромных мусоропроводных трубок'),
    Question('Зачем у сов такие большие глаза?', 'Для охоты ночью на мелких грызунов', 'Мне всё равно', 'Для летания высоко', 'Это ведьмы')
]


# Стили для виджетов
style = '''
    QLabel {
        font-size: 40px;
        color: #333;
    }
    QRadioButton {
        font-size: 25px;
        spacing: 10px;
    }
    QPushButton {
        font-size: 25px;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QGroupBox {
        font-size: 30px;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        margin: 10px;
        padding: 10px;
    }
    QGroupBox:title {
        subcontrol-origin: margin;
        subcontrol-position: top center;
        padding: 0 10px;
    }
'''

# Создание приложения
app = QApplication([])

# Основное окно
window = QWidget()
window.setWindowTitle('Тест на Ориентацию')
window.setStyleSheet(style)
window.resize(700,500)

# Виджеты для формы с вопросом и вариантами ответов
question = QLabel('Какой ты ориентации?')

button_box = QGroupBox('Варианты:')
button1 = QRadioButton('Трансформер')
button2 = QRadioButton('Рептилойд')
button3 = QRadioButton('Двуликий')
button4 = QRadioButton('Восточный')

# Виджеты для формы с результатом
result_box = QGroupBox('Результат:')
result = QLabel('Здесь будет результат')
right_answer = QLabel('Здесь будет правильный ответ')

button_ok = QPushButton('Ответить')

# Расположение виджетов
main_layout = QVBoxLayout()

# Расположение виджетов для формы с вариантами ответов
answer_layout = QVBoxLayout()
button_box.setLayout(answer_layout)
answer_layout.addWidget(button1)
answer_layout.addWidget(button2)
answer_layout.addWidget(button3)
answer_layout.addWidget(button4)

# Расположение виджетов для формы с результатом
result_layout = QVBoxLayout()
result_box.setLayout(result_layout)
result_layout.addWidget(result)
result_layout.addWidget(right_answer)

# Добавление виджетов на основное окно
main_layout.addWidget(question)
main_layout.addWidget(button_box)
main_layout.addWidget(result_box)
main_layout.addWidget(button_ok)


# Функционал для кнопки "Ответить"
buttons = [button1,button2,button3,button4]

def ask(q: Question):
    shuffle(buttons)
    question.setText(q.question)
    buttons[0].setText(q.right_ans)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)

def next():

    button_box.show()
    result_box.hide()
    button_ok.setText('Ответить')

    window.current_question += 1
    if window.current_question >= len(questions):
        window.current_question = 0

    q = questions[window.current_question]
    ask(q)

def check():

    button_box.hide()
    result_box.show()
    button_ok.setText('Следующий вопрос')

    if buttons[0].isChecked():
        result.setText('Правильно')
    else:
        result.setText('Не правильно')

def ok():
    if button_ok.text() == 'Ответить':
        check()
    else:
        next()

# Подключение сигнала нажатия кнопки
button_ok.clicked.connect(ok)

# Изначально скрываем результат
result_box.hide()

# Установка и отображение основного окна
window.current_question = 0
ask(questions[window.current_question])
window.setLayout(main_layout)
window.show()

# Запуск приложения
app.exec()
