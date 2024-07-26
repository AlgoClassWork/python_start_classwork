from PyQt5.QtWidgets import (
    QPushButton, QListWidget, QLabel,
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout)

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.resize(1000,600)
window.setWindowTitle('Photoshop')

# ЗАПУСК
window.show()
app.exec()
