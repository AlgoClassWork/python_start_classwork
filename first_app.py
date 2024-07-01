from random import randint
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QLineEdit,
    QPushButton, QVBoxLayout
)

app = QApplication([])

window = QWidget()
window.setWindowTitle('Игра Угадай Число')
window.resize(600, 400)

# Создание виджетов
text = QLabel('Попробуйте победить меня, я загадал число от 1 до 100')
otvet = QLineEdit()
result = QPushButton('Ответить')

# Расположение виджетов
main_layout = QVBoxLayout()
main_layout.addWidget(text)
main_layout.addWidget(otvet)
main_layout.addWidget(result)
window.setLayout(main_layout)

# CSS стили для виджетов
window.setStyleSheet('''
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
    font-size: 16px;
''')

text.setStyleSheet('''
    color: #333;
    font-weight: bold;
    margin-bottom: 20px;
''')

otvet.setStyleSheet('''
    padding: 10px;
    font-size: 14px;
    border: 2px solid #ccc;
''')

result.setStyleSheet('''
    padding: 10px 20px;
    font-size: 16px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
''')

result.setFixedSize(150, 40)  # Установка фиксированного размера кнопки

# Функционал
def show_result():
    nash_otvet = int(otvet.text())
    if nash_otvet > rand_num:
        text.setText('Загаданное число меньше')
    elif nash_otvet < rand_num:
        text.setText('Загаданное число больше')
    else:
        text.setText('Вы угадали')

# Подписки на события
result.clicked.connect(show_result)

# Запуск приложения
rand_num = randint(1, 100)
window.show()
app.exec()
