from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton
)
from PyQt5.QtCore import Qt

# ИНТЕРФЕЙС
app = QApplication([])

# Создаем основное окно
window = QWidget()
window.setWindowTitle('Тест')

# Настройка стиля
window.setStyleSheet("""
    QWidget {
        background-color: #f3f4f6;  /* Светлый фон */
        border-radius: 10px;
        padding: 20px;
    }
    QLabel {
        color: #3f51b5;  /* Синий текст */
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    QRadioButton {
        margin: 10px 0;
        spacing: 10px;
        color: #424242;  /* Темный цвет для радио-кнопок */
        font-size: 16px;
    }
    QRadioButton::indicator {
        width: 25px;
        height: 25px;
    }
    QRadioButton:hover {
        color: #1976d2;  /* Яркий цвет при наведении */
    }
    QRadioButton:checked {
        color: #d32f2f;  /* Красный цвет для выбранного варианта */
    }
""")

question_label = QLabel('Какого цвета чернокожие?')
rbutton1 = QRadioButton('зеленого')
rbutton2 = QRadioButton('черного')
rbutton3 = QRadioButton('белого')
rbutton4 = QRadioButton('голубого')

# РАЗМЕЩЕНИЕ
main_layout = QVBoxLayout()
main_layout.setAlignment(Qt.AlignTop)
main_layout.addWidget(question_label)
main_layout.addWidget(rbutton1)
main_layout.addWidget(rbutton2)
main_layout.addWidget(rbutton3)
main_layout.addWidget(rbutton4)

window.setLayout(main_layout)

# ЗАПУСК
window.resize(300, 200)
window.show()
app.exec()
