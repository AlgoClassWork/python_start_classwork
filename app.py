from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)

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

#РАЗМЕЩЕНИЕ ВИДЖЕТОВ
layout_card = QVBoxLayout()

layout_card.addWidget(lb_Question)
layout_card.addWidget(RadioGroupBox)

layout_card.addWidget(btn_OK)
#ФУНКЦИОНАЛ

#ПОДПИСКИ

#ЗАПУСК
window.setLayout(layout_card)
window.show()
app.exec()
