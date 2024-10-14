from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout,
    QMessageBox
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
h1_layout = QHBoxLayout() #NEW
h2_layout = QHBoxLayout() #NEW
main_layout.addWidget(question_label)
main_layout.addLayout(h1_layout) #NEW
main_layout.addLayout(h2_layout) #NEW
main_layout.setAlignment(Qt.AlignTop)
h1_layout.addWidget(rbutton1) #UPDATE
h1_layout.addWidget(rbutton2) #UPDATE
h2_layout.addWidget(rbutton3) #UPDATE
h2_layout.addWidget(rbutton4) #UPDATE
window.setLayout(main_layout)
# ФУНКЦИОНАЛ
def win():
    box = QMessageBox()
    box.setText('ВЫ ВЫИГРАЛИ ЛАМБОРГИНИ!')
    box.exec()

def lose():
    box = QMessageBox()
    box.setText('ВЫ ОТПРАВЛЯЕТЕСЬ НА ШАХТУ!')
    box.exec()

# ПОДПИСКИ
rbutton1.clicked.connect(lose)
rbutton2.clicked.connect(win)
rbutton3.clicked.connect(lose)
rbutton4.clicked.connect(lose)
# ЗАПУСК
window.resize(300, 200)
window.show()
app.exec()
