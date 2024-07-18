from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton, QPushButton,
    QGroupBox, QHBoxLayout, QVBoxLayout
)

# Стили для виджетов
style = '''
    QLabel {
        font-size: 40px;
        color: #333;
    }
    QRadioButton {
        font-size: 25px;
        spacing: 10px;
    }
    QPushButton {
        font-size: 25px;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QGroupBox {
        font-size: 30px;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        margin: 10px;
        padding: 10px;
    }
    QGroupBox:title {
        subcontrol-origin: margin;
        subcontrol-position: top center;
        padding: 0 10px;
    }
'''

# Создание приложения
app = QApplication([])

# Основное окно
window = QWidget()
window.setWindowTitle('Тест на Ориентацию')
window.setStyleSheet(style)

# Виджеты для формы с вопросом и вариантами ответов
question = QLabel('Какой ты ориентации?')

button_box = QGroupBox('Варианты:')
button1 = QRadioButton('Трансформер')
button2 = QRadioButton('Рептилойд')
button3 = QRadioButton('Двуликий')
button4 = QRadioButton('Восточный')

# Виджеты для формы с результатом
result_box = QGroupBox('Результат:')
result = QLabel('Здесь будет результат')
right_answer = QLabel('Здесь будет правильный ответ')

button_ok = QPushButton('Ответить')

# Расположение виджетов
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

# Добавление виджетов на основное окно
main_layout.addWidget(question)
main_layout.addWidget(button_box)
main_layout.addWidget(result_box)
main_layout.addWidget(button_ok)

# Функционал для кнопки "Ответить"
def ok():
    if button_ok.text() == 'Ответить':
        button_box.hide()
        result_box.show()
        button_ok.setText('Следующий вопрос')
    else:
        button_box.show()
        result_box.hide()
        button_ok.setText('Ответить')

# Подключение сигнала нажатия кнопки
button_ok.clicked.connect(ok)

# Изначально скрываем результат
result_box.hide()

# Установка и отображение основного окна
window.setLayout(main_layout)
window.show()

# Запуск приложения
app.exec()
