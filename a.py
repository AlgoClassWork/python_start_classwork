from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton
)
# Создание элементов интерфейса
app = QApplication([])
window = QWidget()

question_label = QLabel('Сколько будет 2 + 2?')
answer_button = QPushButton('Ответить')

# Создание формы с вариантами ответов
answers_form = QGroupBox('Варианты ответов:')
rbtn1 = QRadioButton('пять')
rbtn2 = QRadioButton('один')
rbtn3 = QRadioButton('четыре')
rbtn4 = QRadioButton('не знаю')
# Размещение элементов интерфейса
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answers_form) #new
main_layout.addWidget(answer_button)
window.setLayout(main_layout)
# Запуск приложения
window.show()
app.exec()
