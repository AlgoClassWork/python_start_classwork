from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton, QPushButton,
    QGroupBox, QHBoxLayout, QVBoxLayout
)

style = '''
    QLabel {font-size: 30px}
    QRadioButton {font-size: 15px}
    QPushButton {font-size: 30px}
'''

#ИНТЕРФЕЙС
app = QApplication([])

window = QWidget()
window.setWindowTitle('ТЕСТ НА ОРИЕНТАЦИЮ')
window.setStyleSheet(style)

question = QLabel('Какой ты ориентации?')

button1 = QRadioButton('Трансформер')
button2 = QRadioButton('Рептилойд')
button3 = QRadioButton('Двуликий')
button4 = QRadioButton('Восточный')

button_ok = QPushButton('Ответить')

#ЗАПУСК
window.show()
app.exec()
