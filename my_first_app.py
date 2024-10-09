from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout
)
# СОЗДАНИЕ ВИДЖЕТОВ
app = QApplication([])
window = QWidget()
text = QLabel('Нажми чтобы узнать кто нефор')
window.setWindowTitle('Генератор победителя')
# РАЗМЕЩЕНИЕ ВИДЖЕТОВ
line = QVBoxLayout()
line.addWidget(text)
window.setLayout(line)
# ЗАПУСК ПРИЛОЖЕНИЯ
window.show()
app.exec()
