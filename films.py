from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout
)
# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Фильмы')
text_field = QTextEdit()
# РАЗМЕЩЕНИЕ
main_line = QHBoxLayout()
main_line.addWidget(text_field)
window.setLayout(main_line)
# ЗАПУСК
window.show()
app.exec()
