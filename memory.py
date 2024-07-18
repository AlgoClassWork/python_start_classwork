from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton, QPushButton,
    QGroupBox, QHBoxLayout, QVBoxLayout
)

style = '''
    QLabel {font-size: 50px}
    QRadioButton {font-size: 30px}
    QPushButton {font-size: 30px}
    QGroupBox {font-size: 30px}
'''

#ИНТЕРФЕЙС
app = QApplication([])

window = QWidget()
window.setWindowTitle('ТЕСТ НА ОРИЕНТАЦИЮ')
window.setStyleSheet(style)

question = QLabel('Какой ты ориентации?')

#ВИДЖЕТЫ ДЛЯ ФОРМЫ С ВАРИАНТАМИ ОТВЕТОВ
button_box = QGroupBox('Варианты:')
button1 = QRadioButton('Трансформер')
button2 = QRadioButton('Рептилойд')
button3 = QRadioButton('Двуликий')
button4 = QRadioButton('Восточный')

#ВИДЖЕТЫ ДЛЯ ФОРМЫ С РЕЗУЛЬТАТОМ
result_box = QGroupBox('Результат:')
result = QLabel('Здесь будет результат')
right_answer = QLabel('Здесь будет правильный ответ')

button_ok = QPushButton('Ответить')
#РАСПОЛОЖЕНИЕ
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

# Расположение виджетов на главном окне
main_layout.addWidget(question)
main_layout.addWidget(button_box)
main_layout.addWidget(result_box)
main_layout.addWidget(button_ok)

#ЗАПУСК
window.setLayout(main_layout)
window.show()
app.exec()
