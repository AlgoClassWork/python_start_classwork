from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton,
    QVBoxLayout, QGroupBox)

#ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')
window.show()

question_label = QLabel('Как переводится слово Apple?')
answer_button = QPushButton('Ответить')
#СОЗДАНИЕ ФОРМЫ С РЕЗУЛЬТАТОМ
result_form = QGroupBox('Результат:') 
result_label = QLabel('Правильно')
correct_label = QLabel('яблоко')
result_layout = QVBoxLayout()
result_layout.addWidget(result_label)
result_layout.addWidget(correct_label)
result_form.setLayout(result_layout)
#РАЗМЕЩЕНИЕ НА ГЛАВНОМ ЭКРАНЕ
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(result_form) 
main_layout.addWidget(answer_button)
window.setLayout(main_layout)
#ЗАПУСК
result_form.hide()
app.exec()
