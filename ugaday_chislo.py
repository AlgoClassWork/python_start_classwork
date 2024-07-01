from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QVBoxLayout, QLineEdit, QPushButton)

# СОЗДАНИЕ ИНТЕРФЕЙСА
app = QApplication([]) # создание приложения
window = QWidget() # создание окна
text_label = QLabel('Я загадал число от 1 до 100')
input_field = QLineEdit()
result_btn = QPushButton('Ответить')
# РАЗМЕЩЕНИЕ
main_layout = QVBoxLayout()
main_layout.addWidget(text_label)
main_layout.addWidget(input_field)
main_layout.addWidget(result_btn)
window.setLayout(main_layout)
# ФУНКЦИОНАЛ
def show_result():
    pass

# ПОДПИСКИ
result_btn.clicked.connect(show_result)
# ЗАПУСК
window.show()
app.exec()
