from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QLabel, QListWidget, QPushButton, QVBoxLayout)

# ОБЬЕКТЫ ИНТЕРФЕЙСА
app = QApplication([])

window = QWidget()
text_field = QTextEdit()

list_notes_text = QLabel('Список заметок:')
list_notes = QListWidget()
create_note = QPushButton('Создать')
delete_note = QPushButton('Удалить')
save_note = QPushButton('Сохранить')
# РАЗМЕЩЕНИЕ ОБЬЕКТОВ
main_layout = QHBoxLayout()

main_layout.addWidget(text_field)
# ЗАПУСК
window.setLayout(main_layout)
window.show()
app.exec()
