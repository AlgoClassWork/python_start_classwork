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

# Стилизация
app.setStyleSheet("""
    QWidget {
        background-color: #e0e5ec;
        font-family: "Segoe UI", Arial;
        font-size: 16px;
        color: #333;
    }

    QLabel {
        font-size: 18px;
        padding: 5px;
        color: #2a2a2a;
    }

    QGroupBox {
        border: none;
        border-radius: 12px;
        background-color: #e0e5ec;
        padding: 15px;
        margin-top: 15px;
        font-weight: bold;
        color: #2a2a2a;
        box-shadow: inset 3px 3px 7px #bec4cc, inset -3px -3px 7px #ffffff;
    }

    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        top: -7px;
        padding: 0 5px;
        background-color: #e0e5ec;
    }

    QRadioButton {
        spacing: 12px;
        padding: 8px;
        border-radius: 6px;
    }

    QRadioButton:hover {
        background-color: #d6dbdf;
    }

    QPushButton {
        background-color: #4a90e2;
        color: white;
        padding: 10px 18px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #3f7fc1;
    }

    QPushButton:pressed {
        background-color: #356aad;
    }
""")

# Запуск приложения
group_result.hide()
window.show()
app.exec()
