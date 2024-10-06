from PyQt5.QtWidgets import (
    QApplication, QWidget , QLabel, QVBoxLayout, QRadioButton
)
# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест')
window.show()

question_text = QLabel('Какого цвета негр?')
button1 = QRadioButton('белый')
button2 = QRadioButton('черный')
button3 = QRadioButton('зеленый')
button4 = QRadioButton('голубой')
# СТИЛИЗАЦИЯ
question_text.setStyleSheet('font-size:30px')
window.setStyleSheet('QRadioButton {font-size:30px}')
# РАЗМЕЩЕНИЕ
main_line = QVBoxLayout()
main_line.addWidget(question_text)
main_line.addWidget(button1)
main_line.addWidget(button2)
main_line.addWidget(button3)
main_line.addWidget(button4)
window.setLayout(main_line)
# ЗАПУСК
app.exec()
