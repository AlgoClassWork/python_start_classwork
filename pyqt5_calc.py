import os
import PyQt5

# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                            QVBoxLayout, QPushButton, QHBoxLayout)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор')
window.resize(400, 400)

output = QLineEdit()
output.setReadOnly(True)
output.setObjectName("display")

button0 = QPushButton('0')
button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')
button6 = QPushButton('6')
button7 = QPushButton('7')
button8 = QPushButton('8')
button9 = QPushButton('9')

button_plus = QPushButton('+')
button_minus = QPushButton('-')
button_multiply = QPushButton('*')
button_divide = QPushButton('/')

button_equal = QPushButton('=')
button_clear = QPushButton('C')

# назначаем классы для цвета
for b in [button_plus, button_minus, button_multiply, button_divide]:
    b.setProperty("class", "operator")

button_equal.setProperty("class", "equal")
button_clear.setProperty("class", "clear")

# Layout
main_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
h3_layout = QHBoxLayout()
h4_layout = QHBoxLayout()
h5_layout = QHBoxLayout()

main_layout.addWidget(output)
main_layout.addLayout(h1_layout)
main_layout.addLayout(h2_layout)
main_layout.addLayout(h3_layout)
main_layout.addLayout(h4_layout)
main_layout.addLayout(h5_layout)

h1_layout.addWidget(button1)
h1_layout.addWidget(button2)
h1_layout.addWidget(button3)
h1_layout.addWidget(button_plus)

h2_layout.addWidget(button4)
h2_layout.addWidget(button5)
h2_layout.addWidget(button6)
h2_layout.addWidget(button_minus)

h3_layout.addWidget(button7)
h3_layout.addWidget(button8)
h3_layout.addWidget(button9)
h3_layout.addWidget(button_multiply)

h4_layout.addWidget(button0)
h4_layout.addWidget(button_divide)

h5_layout.addWidget(button_equal)
h5_layout.addWidget(button_clear)

window.setLayout(main_layout)

# СТИЛЬ
app.setStyleSheet("""
QWidget{
    background-color: #1e1e1e;
}

QLineEdit#display{
    background-color: #2b2b2b;
    color: white;
    font-size: 28px;
    padding: 15px;
    border-radius: 10px;
}

QPushButton{
    background-color: #3a3a3a;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 15px;
}

QPushButton:hover{
    background-color: #505050;
}

QPushButton[class="operator"]{
    background-color: #ff9500;
}

QPushButton[class="operator"]:hover{
    background-color: #ffaa33;
}

QPushButton[class="equal"]{
    background-color: #34c759;
    font-size: 22px;
}

QPushButton[class="equal"]:hover{
    background-color: #45d96b;
}

QPushButton[class="clear"]{
    background-color: #ff3b30;
}

QPushButton[class="clear"]:hover{
    background-color: #ff5c52;
}
""")

# Логика калькулятора
def on_button_clicked(value):
    current_text = output.text()
    new_text = current_text + value
    output.setText(new_text)

def on_equal_clicked():
    try:
        result = eval(output.text())
        output.setText(str(result)) 
    except Exception:
        output.setText("Ошибка")
    
    
# Подписки на кнопки
button0.clicked.connect(lambda: on_button_clicked('0'))
button1.clicked.connect(lambda: on_button_clicked('1'))
button2.clicked.connect(lambda: on_button_clicked('2'))
button3.clicked.connect(lambda: on_button_clicked('3'))
button4.clicked.connect(lambda: on_button_clicked('4'))
button5.clicked.connect(lambda: on_button_clicked('5'))
button6.clicked.connect(lambda: on_button_clicked('6'))
button7.clicked.connect(lambda: on_button_clicked('7'))
button8.clicked.connect(lambda: on_button_clicked('8'))
button9.clicked.connect(lambda: on_button_clicked('9'))
button_plus.clicked.connect(lambda: on_button_clicked('+'))
button_minus.clicked.connect(lambda: on_button_clicked('-'))
button_multiply.clicked.connect(lambda: on_button_clicked('*'))
button_divide.clicked.connect(lambda: on_button_clicked('/'))
button_equal.clicked.connect(on_equal_clicked)
button_clear.clicked.connect(lambda: output.setText(''))

window.show()
app.exec()
