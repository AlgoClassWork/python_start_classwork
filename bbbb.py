from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton,
    QVBoxLayout, QGroupBox,
    QRadioButton, QHBoxLayout)

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.setStyleSheet("""
    QWidget {
        background-color: #f8f9fa; 
        font-family: Arial, sans-serif;
    }
    QLabel {
        font-size: 16px;
        margin: 5px 0;
    }
    #question {
        font-size: 20px; 
        font-weight: bold; 
        margin: 20px 0;
    }
    QPushButton {
        background-color: #007bff; 
        color: white; 
        font-size: 16px; 
        padding: 10px; 
        border: none; 
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px; 
    }
    QPushButton:hover {
        background-color: #0056b3;
    }
    QGroupBox {
        font-size: 16px; 
        margin-bottom: 20px;
        padding: 10px;  
        border: 1px solid #ced4da;
        border-radius: 5px;
    }
    QRadioButton {
        font-size: 16px; 
        margin-right: 10px;
    }
    #resultLabel {
        font-weight: bold;
    }
    QGroupBox#result {
        margin-top: 20px;
        border: 1px solid #ced4da;
    }
""")

# Заголовок вопроса
question_label = QLabel('Как переводится слово Apple?')
question_label.setObjectName('question')

# Кнопка ответа
answer_button = QPushButton('Ответить')

# Создание формы с ответами
answers_form = QGroupBox('Варианты:')
button1 = QRadioButton('собака')
button2 = QRadioButton('банан')
button3 = QRadioButton('яблоко')
button4 = QRadioButton('ноутбук')
answers_layout = QVBoxLayout()
h1, h2 = QHBoxLayout(), QHBoxLayout()
answers_layout.addLayout(h1)
answers_layout.addLayout(h2)
h1.addWidget(button1)
h1.addWidget(button2)
h2.addWidget(button3)
h2.addWidget(button4)
answers_form.setLayout(answers_layout)

# Создание формы с результатом
result_form = QGroupBox('Результат:')
result_form.setObjectName('result')
result_label = QLabel('Правильно')
result_label.setObjectName('resultLabel')
correct_label = QLabel('яблоко')
result_layout = QVBoxLayout()
result_layout.addWidget(result_label)
result_layout.addWidget(correct_label)
result_form.setLayout(result_layout)

# Размещение на главном экране
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answers_form)
main_layout.addWidget(result_form)
main_layout.addWidget(answer_button)

# Настройка отступов для основного лэйаута
main_layout.setContentsMargins(20, 20, 20, 20)
main_layout.setSpacing(15)

window.setLayout(main_layout)

# Запуск
result_form.hide()
window.show()
app.exec()
