from random import randint
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QLineEdit,
    QPushButton, QVBoxLayout)

#ИНТЕРФЕЙС
app = QApplication([])

window = QWidget()
window.setWindowTitle('Игра Угадай Число')
window.resize(600,400)

text = QLabel('Попробуй победить меня я загадал число от 1 до 100')
otvet = QLineEdit() # new
result = QPushButton('Ответить')
#РАСПОЛОЖЕНИЕ
main_line = QVBoxLayout()
main_line.addWidget(text)
main_line.addWidget(otvet) # new
main_line.addWidget(result)

window.setLayout(main_line)

#Функционал
def show_result():
    nash_otvet = int( otvet.text() )
    if nash_otvet > rand_num:
        text.setText('Загаданое число меньше')
    elif nash_otvet < rand_num:
        text.setText('Загаданое число больше')
    else:
        text.setText('Вы угадали')

#Подписки на события
result.clicked.connect(show_result)
#ЗАПУСК
rand_num = randint(1,100)
window.show()
app.exec()
