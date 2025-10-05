from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit
)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор')
window.setStyleSheet("""
    QWidget {
        background-color: #2E3440;
    }

    QLineEdit {
        padding: 20px;
        font-size: 30px;
        background-color: #3B4252;
        color: #ECEFF4;
        border: none;
        border-radius: 10px;
    }

    QPushButton {
        font-size: 20px;
        padding: 15px;
        background-color: #4C566A;
        color: #ECEFF4;
        border: none;
        border-radius: 10px;
    }

    QPushButton:hover {
        background-color: #5E81AC;
    }

    QPushButton:pressed {
        background-color: #81A1C1;
    }

    QPushButton#equal {
        background-color: #A3BE8C;
        color: black;
    }

    QPushButton#equal:hover {
        background-color: #B5CEA8;
    }

    QPushButton#reset {
        background-color: #BF616A;
    }

    QPushButton#reset:hover {
        background-color: #D08770;
    }
""")

# Поле с операциями
operation_field = QLineEdit()
operation_field.setReadOnly(True)

# Кнопки
def create_button(text, object_name=""):
    btn = QPushButton(text)
    if object_name:
        btn.setObjectName(object_name)
    return btn

button_0 = create_button('0')
button_1 = create_button('1')
button_2 = create_button('2')
button_3 = create_button('3')
button_4 = create_button('4')
button_5 = create_button('5')
button_6 = create_button('6')
button_7 = create_button('7')
button_8 = create_button('8')
button_9 = create_button('9')

button_plus = create_button('+')
button_minus = create_button('-')
button_multiply = create_button('*')
button_devide = create_button('/')

button_reset = create_button('C', 'reset')
button_equal = create_button('=', 'equal')

# Размещение
main_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
h4_line = QHBoxLayout()

main_line.addWidget(operation_field)
main_line.addLayout(h1_line)
main_line.addLayout(h2_line)
main_line.addLayout(h3_line)
main_line.addLayout(h4_line)

h1_line.addWidget(button_1)
h1_line.addWidget(button_2)
h1_line.addWidget(button_3)
h1_line.addWidget(button_plus)

h2_line.addWidget(button_4)
h2_line.addWidget(button_5)
h2_line.addWidget(button_6)
h2_line.addWidget(button_minus)

h3_line.addWidget(button_7)
h3_line.addWidget(button_8)
h3_line.addWidget(button_9)
h3_line.addWidget(button_multiply)

h4_line.addWidget(button_reset)
h4_line.addWidget(button_0)
h4_line.addWidget(button_equal)
h4_line.addWidget(button_devide)

# Функционал
def button_text(symbol, operation_field):
    current_text = operation_field.text()
    new_text = current_text + symbol
    operation_field.setText(new_text)

def clear_field(operation_field):
    operation_field.clear()

# Подписки на события
button_0.clicked.connect( lambda: button_text('0', operation_field) )
button_1.clicked.connect( lambda: button_text('1', operation_field) )
button_2.clicked.connect( lambda: button_text('2', operation_field) )
button_3.clicked.connect( lambda: button_text('3', operation_field) )
button_4.clicked.connect( lambda: button_text('4', operation_field) )
button_5.clicked.connect( lambda: button_text('5', operation_field) )
button_6.clicked.connect( lambda: button_text('6', operation_field) )
button_7.clicked.connect( lambda: button_text('7', operation_field) )
button_8.clicked.connect( lambda: button_text('8', operation_field) )
button_9.clicked.connect( lambda: button_text('9', operation_field) )
button_plus.clicked.connect( lambda: button_text('+', operation_field) )
button_minus.clicked.connect( lambda: button_text('-', operation_field) )
button_multiply.clicked.connect( lambda: button_text('*', operation_field) )
button_devide.clicked.connect( lambda: button_text('/', operation_field) )

button_reset.clicked.connect( lambda: clear_field(operation_field) )

window.setLayout(main_line)
window.resize(500, 300)
window.show()
app.exec()
