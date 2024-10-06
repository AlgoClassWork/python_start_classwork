from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton,
    QVBoxLayout, QHBoxLayout,
    QMessageBox
)
# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест на слабоумие')
question = QLabel('Какого цвета чернокожие?')
button1 = QRadioButton('белые')
button2 = QRadioButton('коричневые')
button3 = QRadioButton('голубые')
button4 = QRadioButton('серые')
# РАЗМЕЩЕНИЕ
line = QVBoxLayout()
line.addWidget(question)
line.addWidget(button1)
line.addWidget(button2)
line.addWidget(button3)
line.addWidget(button4)
window.setLayout(line)
# ЗАПУСК
window.show()
app.exec()

