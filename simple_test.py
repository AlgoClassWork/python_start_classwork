from PyQt5.QtWidgets import (
    QApplication, QWidget , QLabel, QVBoxLayout, QRadioButton,
    QHBoxLayout
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
top_btn_line = QHBoxLayout()
bot_btn_line = QHBoxLayout()
main_line.addWidget(question_text)
main_line.addLayout(top_btn_line)
top_btn_line.addWidget(button1)
top_btn_line.addWidget(button2)
main_line.addLayout(bot_btn_line)
bot_btn_line.addWidget(button3)
bot_btn_line.addWidget(button4)
window.setLayout(main_line)
# ЗАПУСК
app.exec()
