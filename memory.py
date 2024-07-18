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

main_layout.addWidget(question)
main_layout.addWidget(button_box)
main_layout.addWidget(button_ok)

#ЗАПУСК
window.setLayout(main_layout)
window.show()
app.exec()
