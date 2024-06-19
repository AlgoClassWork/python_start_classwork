from PyQt5.QtWidgets import (
        QApplication, QWidget, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)

#БАЗА ДАННЫХ
class Question():
    def __init__(self,question,right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Когда родился Австрийский художник','568','1350','888','1488'))
question_list.append(Question('Почему небо голубое','из за Голубей','низнаю','хз','потому что'))
question_list.append(Question('Почему в рф запретили голубой цвет','потому что его нет на флаге','из за голубей','захотелось','низнаю'))
       


#ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400, 300)

btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса
#ФОРМА С ВАРИАНТАМИ ОТВЕТОВ
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans2.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans2.addWidget(rbtn_4)

RadioGroupBox.setLayout(layout_ans2) # готова "панель" с вариантами ответов 
#ФОРМА С РЕЗУЛЬТАТОМ
AnsGroupBox = QGroupBox("Результаты теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
#РАЗМЕЩЕНИЕ ВИДЖЕТОВ
layout_card = QVBoxLayout()

layout_card.addWidget(lb_Question)
layout_card.addWidget(RadioGroupBox)
layout_card.addWidget(AnsGroupBox)
layout_card.addWidget(btn_OK)
#ФУНКЦИОНАЛ

def check_answer():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def next_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос

#ПОДПИСКИ
btn_OK.clicked.connect(click_OK)

#ЗАПУСК
window.setLayout(layout_card)
window.show()
app.exec()
