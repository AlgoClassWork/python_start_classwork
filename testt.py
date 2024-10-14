from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout
)
# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест')
window.show()

question_label = QLabel('Какого цвета чернокожие?')
# РАЗМЕЩЕНИЕ
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
window.setLayout(main_layout)
# ЗАПУСК
app.exec()
