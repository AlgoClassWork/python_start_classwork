from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton,
    QVBoxLayout, QHBoxLayout
)

stylesheet = """
QWidget {
    background-color: white;  /* Светло-голубой фон */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;  /* Шрифт */
}

QLabel {
    font-size: 24px;  /* Размер шрифта для QLabel */
    color: black;  /* Цвет текста */
    margin: 20px;  /* Отступы вокруг QLabel */
    text-align: center;  /* Выравнивание текста по центру */
}

QRadioButton {
    font-size: 20px;  /* Размер шрифта для QRadioButton */
    color: black;  /* Цвет текста */
    padding: 10px;  /* Отступы вокруг текста */
}

QRadioButton::indicator {
    width: 25px;  /* Ширина индикатора */
    height: 25px;  /* Высота индикатора */
}

QRadioButton::indicator:checked {
    background-color: #004d40;  /* Цвет индикатора при выборе */
    border: 3px solid #004d40;  /* Граница индикатора при выборе */
}

QRadioButton::indicator:unchecked {
    background-color: #ffffff;  /* Цвет индикатора при невыборе */
    border: 3px solid #00796b;  /* Граница индикатора при невыборе */
}

QRadioButton::indicator:pressed {
    background-color: #b2dfdb;  /* Цвет индикатора при нажатии */
}

QVBoxLayout, QHBoxLayout {
    spacing: 15px;  /* Расстояние между элементами в макете */
}
"""

# Интерфейс
app = QApplication([])
window = QWidget()

text = QLabel('Какого цвета негр?')

button1 = QRadioButton('белый')
button2 = QRadioButton('зеленый')
button3 = QRadioButton('черный')
button4 = QRadioButton('синий')

# Размещение
main_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()

main_line.addWidget(text)

h1_line.addWidget(button1)
h1_line.addWidget(button2)

h2_line.addWidget(button3)
h2_line.addWidget(button4)

main_line.addLayout(h1_line)
main_line.addLayout(h2_line)

window.setLayout(main_line)

# Применение стилей
window.setStyleSheet(stylesheet)

# Функционал

# Подписки на события

# Запуск
window.show()
app.exec()
