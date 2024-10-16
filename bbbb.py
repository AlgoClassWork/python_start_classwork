from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton,
    QVBoxLayout)

#ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')
window.show()

question_label = QLabel('Как переводится слово Apple?')
answer_button = QPushButton('Ответить')
#РАЗМЕЩЕНИЕ НА ГЛАВНОМ ЭКРАНЕ
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answer_button)
window.setLayout(main_layout)
#ЗАПУСК
app.exec()
