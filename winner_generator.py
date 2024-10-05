# pip install pyqt5
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)

app = QApplication([])
window = QWidget()

window.show()
app.exec()

