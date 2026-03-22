from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QRadioButton, QGroupBox, QPushButton,
    QVBoxLayout, QHBoxLayout
)
# Созднание элементов интерфейса
app = QApplication([])
window = QWidget()
window.setWindowTitle('Викторина')

question_label = QLabel('Самая высокая гора в мире?')
button = QPushButton('Ответить')
# Группа для ответов
answer_group = QGroupBox('Ответы')
answer1_radio = QRadioButton('Эверест')
answer2_radio = QRadioButton('Килиманджаро')
answer3_radio = QRadioButton('Макалу')
answer4_radio = QRadioButton('Лхоцзе')
answer_layout = QVBoxLayout()
answer_h1_layout = QHBoxLayout()
answer_h2_layout = QHBoxLayout()
answer_layout.addLayout(answer_h1_layout)
answer_layout.addLayout(answer_h2_layout)
answer_h1_layout.addWidget(answer1_radio)
answer_h1_layout.addWidget(answer2_radio)
answer_h2_layout.addWidget(answer3_radio)
answer_h2_layout.addWidget(answer4_radio)
answer_group.setLayout(answer_layout)
# Группа для результата
result_group = QGroupBox('Результат')
result_label = QLabel('Правильный ответ: Эверест')
result_layout = QVBoxLayout()
result_layout.addWidget(result_label)
result_group.setLayout(result_layout)
# Расположение элементов интерфейса
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answer_group)
main_layout.addWidget(result_group)
main_layout.addWidget(button)
window.setLayout(main_layout)
# Стилизация элементов интерфейса
answer_group.setStyleSheet('background-color: white;')
# Запуск приложения
result_group.hide()
window.show()
app.exec()
