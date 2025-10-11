from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel, QGroupBox, 
    QRadioButton, QPushButton
)
# Создание обьектов интерфейса
app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест на слабоумие')

label_question = QLabel('Как тебя зовут?')
button_ok = QPushButton('Ответить')

# Форма с вариантами ответов
group_answer = QGroupBox('Варианты ответов')
rbutton1 = QRadioButton('Забыл')
rbutton2 = QRadioButton('Зеленый')
rbutton3 = QRadioButton('Сорок семь')
rbutton4 = QRadioButton('Тут нет моего имени')

# Форма с результатами
group_result = QGroupBox('Результаты')
label_result = QLabel('Верно')
label_correct = QLabel('Тут нет моего имени')

# Размещение обьектов интерфейса
line_main = QVBoxLayout()

# Размещение для формы с вариантами ответов
line_answer_main = QVBoxLayout()
line_answer_h1 = QHBoxLayout()
line_answer_h2 = QHBoxLayout()
line_answer_main.addLayout(line_answer_h1)
line_answer_main.addLayout(line_answer_h2)
line_answer_h1.addWidget(rbutton1)
line_answer_h1.addWidget(rbutton2)
line_answer_h2.addWidget(rbutton3)
line_answer_h2.addWidget(rbutton4)
group_answer.setLayout(line_answer_main)

# Размещение для формы с результатами
line_result_main = QVBoxLayout()
line_result_main.addWidget(label_result)
line_result_main.addWidget(label_correct)
group_result.setLayout(line_result_main)

# Размещение всех виджетов
line_main.addWidget(label_question)
line_main.addWidget(group_answer)
line_main.addWidget(group_result)
line_main.addWidget(button_ok)

window.setLayout(line_main)

# Запуск приложения
group_result.hide()
window.show()
app.exec()
