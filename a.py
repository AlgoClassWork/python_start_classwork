from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton
)

style_sheet = """
QWidget {
    background-color: #e9ecef;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 16px;
    color: #343a40;
}

QLabel {
    font-weight: bold;
    margin-bottom: 10px;
}

QPushButton {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    font-weight: bold;
    transition: background-color 0.3s;
}

QPushButton:hover {
    background-color: #0056b3;
}

QGroupBox {
    background-color: #ffffff;
    border: 2px solid #ced4da;
    border-radius: 10px;
    margin-top: 20px;
    padding: 15px;
}

QRadioButton {
    margin: 5px;
    font-size: 14px;
}

QRadioButton::indicator {
    width: 25px;
    height: 25px;
}

QRadioButton::indicator:checked {
    background-color: #007bff;
    border: 2px solid #007bff;
}

QRadioButton::indicator:unchecked {
    background-color: #ffffff;
    border: 2px solid #ced4da;
}

QVBoxLayout, QHBoxLayout {
    spacing: 12px;
}

QLineEdit {
    border: 2px solid #ced4da;
    border-radius: 8px;
    padding: 10px;
}

QLineEdit:focus {
    border: 2px solid #007bff;
    background-color: #f8f9fa;
}
"""

# Создание элементов интерфейса
app = QApplication([])
window = QWidget()
window.setStyleSheet(style_sheet)
question_label = QLabel('Сколько будет 2 + 2?')
answer_button = QPushButton('Ответить')

# Создание формы с вариантами ответов
answers_form = QGroupBox('Варианты ответов:')
rbtn1 = QRadioButton('пять')
rbtn2 = QRadioButton('один')
rbtn3 = QRadioButton('четыре')
rbtn4 = QRadioButton('не знаю')
v_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h1_line.addWidget(rbtn1)
h1_line.addWidget(rbtn2)
h2_line.addWidget(rbtn3)
h2_line.addWidget(rbtn4)
v_line.addLayout(h1_line)
v_line.addLayout(h2_line)
answers_form.setLayout(v_line)
# Создание формы с результатами
results_form = QGroupBox('Ваши результаты:')
result_label = QLabel('Правильно')
correct_label = QLabel('четыре')
line = QVBoxLayout()
line.addWidget(result_label)
line.addWidget(correct_label)
results_form.setLayout(line)
# Размещение элементов интерфейса
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answers_form)
main_layout.addWidget(results_form)
main_layout.addWidget(answer_button)
window.setLayout(main_layout)
# Функционал приложения
def change_form():
    if answer_button.text() == 'Ответить':
        answers_form.hide()
        results_form.show()
        answer_button.setText('Следующий вопрос')
    else:
        answers_form.show()
        results_form.hide()
        answer_button.setText('Ответить')

# Подписки на события
answer_button.clicked.connect(change_form)
# Запуск приложения
results_form.hide()
window.show()
app.exec()
