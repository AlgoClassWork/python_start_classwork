from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout)

# ОБЬЕКТЫ ИНТЕРФЕЙСА
app = QApplication([])

window = QWidget()
text_field = QTextEdit()

# РАЗМЕЩЕНИЕ ОБЬЕКТОВ
main_layout = QHBoxLayout()

main_layout.addWidget(text_field)
# ЗАПУСК
window.setLayout(main_layout)
window.show()
app.exec()
