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
line = QVBoxLayout() # главная вертикальная линия
top_h_line = QHBoxLayout() # горизонтальная линия две верхних кнопок
bot_h_line = QHBoxLayout() # горизонтальная линия две нижних кнопок
line.addWidget(question)
top_h_line.addWidget(button1)
top_h_line.addWidget(button2)
line.addLayout(top_h_line)
bot_h_line.addWidget(button3)
bot_h_line.addWidget(button4)
line.addLayout(bot_h_line)
window.setLayout(line)
# ЗАПУСК
window.show()
app.exec()

