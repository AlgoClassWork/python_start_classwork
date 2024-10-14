from PyQt5.QtWidgets import (
    QApplication, QWidget
)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест')
window.show()
app.exec()
