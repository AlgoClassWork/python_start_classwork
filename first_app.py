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
#РАСПОЛОЖЕНИЕ
main_line = QVBoxLayout()
main_line.addWidget(text)
window.setLayout(main_line)
#ЗАПУСК
window.show()
app.exec()
