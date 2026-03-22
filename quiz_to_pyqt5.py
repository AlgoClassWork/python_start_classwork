from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QRadioButton, QGroupBox, QPushButton,
    QVBoxLayout, QHBoxLayout
)
# Созднание элементов интерфейса
app = QApplication([])
window = QWidget()
window.setWindowTitle('Викторина')

question_label = QLabel('Самая высокая гора в мире?')

# Группа для ответов
answer_group = QGroupBox('Ответы')
answer1_radio = QRadioButton('Эверест')
answer2_radio = QRadioButton('Килиманджаро')
answer3_radio = QRadioButton('Макалу')
answer4_radio = QRadioButton('Лхоцзе')
answer_layout = QVBoxLayout()
answer_layout.addWidget(answer1_radio)
answer_layout.addWidget(answer2_radio)
answer_layout.addWidget(answer3_radio)
answer_layout.addWidget(answer4_radio)
answer_group.setLayout(answer_layout)
# Расположение элементов интерфейса
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answer_group)
window.setLayout(main_layout)

# Стилизация элементов интерфейса
answer_group.setStyleSheet('background-color: white;')

# Запуск приложения
window.show()
app.exec()
