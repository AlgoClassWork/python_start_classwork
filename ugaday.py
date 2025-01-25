from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# Создание приложения и экрана
app = QApplication([])

window = QWidget()
window.setWindowTitle('Угадай число')

# Создание виджетов (элементы интерфейса)
game_label = QLabel('Игра угадай число')
text_input = QLineEdit()
text_input.setPlaceholderText('Введите число')
button = QPushButton('Нажми на меня')

# Размещение виджетов
line = QVBoxLayout()
line.addWidget(game_label)
line.addWidget(text_input)
line.addWidget(button)
window.setLayout(line)

# CSS для улучшения внешнего вида
window.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    QLabel {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        text-align: center;
    }
    QLineEdit {
        font-size: 16px;
        padding: 10px;
        background-color: #fff;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    QPushButton {
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 5px;
        border: none;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QVBoxLayout {
        margin: 20px;
        spacing: 20px;
    }
""")

def result():
    num = int(text_input.text())
    text_input.clear()
    if num > win_num:
        game_label.setText('Загаданное число меньше')
    elif num < win_num:
        game_label.setText('Загаданное число больше')
    else:
        game_label.setText('Вы выйграли пачку сухариков')

# Подписки на события
button.clicked.connect(result)
# Запуск приложения
win_num = randint(1,100)
window.resize(400,200)
window.show()
app.exec()
