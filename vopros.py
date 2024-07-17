from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton,
    QVBoxLayout, QHBoxLayout,
    QMessageBox
)

#ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()

text = QLabel('Какого цвета негр?')

button1 = QRadioButton('белый')
button2 = QRadioButton('зеленый')
button3 = QRadioButton('черный')
button4 = QRadioButton('синий')
#РАЗМЕЩЕНИЕ
main_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()

main_line.addWidget(text)

main_line.addLayout(h1_line)
main_line.addLayout(h2_line)

h1_line.addWidget(button1)
h1_line.addWidget(button2)

h2_line.addWidget(button3)
h2_line.addWidget(button4)

window.setLayout(main_line)
#ЗАПУСК
window.show()
app.exec()
