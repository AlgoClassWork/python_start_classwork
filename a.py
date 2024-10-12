from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)
# Создание элементов интерфейса
app = QApplication([])
window = QWidget()

question_label = QLabel('Сколько будет 2 + 2?')
answer_button = QPushButton('Ответить')

# Размещение элементов интерфейса
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(answer_button)
window.setLayout(main_layout)
# Запуск приложения
window.show()
app.exec()
