from PyQt5.QtWidgets import (
    QApplication, QWidget
)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Фильмы')

window.show()
app.exec()
