import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QLabel, QListWidget, QPushButton, QLineEdit, QVBoxLayout)

# ОБЬЕКТЫ ИНТЕРФЕЙСА
app = QApplication([])

window = QWidget()
window.resize(800, 500)
window.setWindowTitle('Заметки')

text_field = QTextEdit()

list_notes_text = QLabel('Список заметок:')
list_notes = QListWidget()
create_note = QPushButton('Создать')
delete_note = QPushButton('Удалить')
save_note = QPushButton('Сохранить')

list_tags_text = QLabel('Список тегов:')
list_tags = QListWidget()
search_field = QLineEdit()
search_field.setPlaceholderText('Введите тег . . .')
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

# СТИЛИЗАЦИЯ

window.setStyleSheet('''
    QWidget {
        background-color: #f0f0f0;
    }
    
    QTextEdit {
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
        padding: 8px;
    }
    
    QListWidget {
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
        padding: 8px;
    }
    
    QPushButton {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 5px 10px;
        text-align: center;
        text-decoration: none;
        font-size: 14px;
        margin: 4px 2px;
        border-radius: 4px;
    }
    
    QPushButton:hover {
        background-color: #45a049;
    }
    
    QLineEdit {
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
        padding: 6px;
    }
    
    QLabel {
        font-size: 16px;
        font-weight: bold;
    } ''')

# ЗАПУСК

with open('notes.json','r',encoding='utf-8') as file:
    notes = json.load(file)

list_notes.addItems(notes)

window.setLayout(main_layout)
window.show()
app.exec()
