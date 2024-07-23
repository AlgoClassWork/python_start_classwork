from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QLabel, QListWidget, QPushButton, QLineEdit, QVBoxLayout)

# ОБЬЕКТЫ ИНТЕРФЕЙСА
app = QApplication([])

window = QWidget()
text_field = QTextEdit()

list_notes_text = QLabel('Список заметок:')
list_notes = QListWidget()
create_note = QPushButton('Создать')
delete_note = QPushButton('Удалить')
save_note = QPushButton('Сохранить')

list_tags_text = QLabel('Список тегов:')
list_tags = QListWidget()
search_field = QLineEdit()
create_tag = QPushButton('Создать')
delete_tag = QPushButton('Удалить')
search = QPushButton('Поиск')

# РАЗМЕЩЕНИЕ ОБЬЕКТОВ
main_layout = QHBoxLayout()
v_line = QVBoxLayout()
h1_line = QHBoxLayout() 
h2_line = QHBoxLayout() 

main_layout.addWidget(text_field)
main_layout.addLayout(v_line)

h1_line.addWidget(create_note) 
h1_line.addWidget(delete_note) 

v_line.addWidget(list_notes_text)
v_line.addWidget(list_notes)
v_line.addLayout(h1_line) 
v_line.addWidget(save_note)

h2_line.addWidget(create_tag)
h2_line.addWidget(delete_tag)

v_line.addWidget(list_tags_text)
v_line.addWidget(list_tags)
v_line.addWidget(search_field)
v_line.addLayout(h2_line)
v_line.addWidget(search)

# ЗАПУСК
window.setLayout(main_layout)
window.show()
app.exec()
