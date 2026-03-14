import os
import PyQt5

# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QFrame, QMessageBox

app = QApplication([])

window = QWidget()
window.setWindowTitle("Конкурс")
window.setGeometry(1000, 500, 800, 600)

# Карточка
card = QFrame()

# Вопрос
question_label = QLabel("Вопрос: Какого цвета чернокожие?")
question_label.setObjectName("question")

# Варианты
option_a = QRadioButton("А) Черные")
option_b = QRadioButton("Б) Белые")
option_c = QRadioButton("В) Зеленые")
option_d = QRadioButton("Г) Красные")

# Layout
main_layout = QVBoxLayout()
card_layout = QVBoxLayout()

h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()

h1_layout.addWidget(option_a)
h1_layout.addWidget(option_b)

h2_layout.addWidget(option_c)
h2_layout.addWidget(option_d)

card_layout.addWidget(question_label)
card_layout.addLayout(h1_layout)
card_layout.addLayout(h2_layout)

card.setLayout(card_layout)

main_layout.addStretch()
main_layout.addWidget(card)
main_layout.addStretch()

window.setLayout(main_layout)

# Стили
window.setStyleSheet("""
QWidget{
    background-color:#1e1e2f;
    font-family:Segoe UI;
}

QFrame{
    background-color:white;
    border-radius:15px;
    padding:50px;
}

QLabel#question{
    font-size:35px;
    font-weight:bold;
    color:black;
}

QRadioButton{
    background-color:#3a3a5a;
    padding:30px;
    border-radius:15px;
    font-size:25px;
    color:white;
}

QRadioButton:hover{
    background-color:#5050a0;
}

QRadioButton::indicator{
    width:18px;
    height:18px;
}

QRadioButton::indicator:checked{
    background-color:#6c8cff;
    border-radius:9px;
}
""")
# Функция для обработки выбора ответа
def correct_answer():
    QMessageBox.information(window, "Ответ", "Правильно!")

def wrong_answer():
    QMessageBox.information(window, "Ответ", "Неправильно!")

# Подключить функцию к каждому варианту
option_a.clicked.connect(correct_answer)
option_b.clicked.connect(wrong_answer)
option_c.clicked.connect(wrong_answer)
option_d.clicked.connect(wrong_answer)
# Показать окно
window.show()
app.exec()
