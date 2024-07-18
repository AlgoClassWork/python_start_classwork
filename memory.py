from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton, QPushButton,
    QGroupBox, QHBoxLayout, QVBoxLayout
)

style = '''
    QLabel {font-size: 50px}
    QRadioButton {font-size: 30px}
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
#РАСПОЛОЖЕНИЕ
main_layout = QVBoxLayout()

main_layout.addWidget(question)
main_layout.addWidget(button1)
main_layout.addWidget(button2)
main_layout.addWidget(button3)
main_layout.addWidget(button4)
main_layout.addWidget(button_ok)

#ЗАПУСК
window.setLayout(main_layout)
window.show()
app.exec()
