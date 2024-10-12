from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)
# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')

question_label = QLabel('Как переводится слово яблоко?')
answer_button = QPushButton('Ответить')
# РАЗМЕЩЕНИЕ
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answer_button)
window.setLayout(main_layout)
# ЗАПУСК
window.show()
app.exec()
