from PyQt5.QtWidgets import (
    QApplication, QWidget
)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')
window.show()

app.exec()
