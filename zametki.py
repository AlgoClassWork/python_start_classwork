import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QLabel, QListWidget, QPushButton, QLineEdit, QVBoxLayout,
    QInputDialog)

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

# ФУНКЦИОНАЛ
def show_note():
    note_name = list_notes.selectedItems()[0].text() 
    text_field.setText(notes[note_name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[note_name]['теги'])

def note_create():
    note_name, ok = QInputDialog().getText(window,'Добавить заметку','Название заметки:')
    if note_name != "":
        notes[note_name] = {"текст": "", "теги": []}
        list_notes.addItem(note_name)
        with open('notes.json','w',encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)

def note_save():
    if list_notes.selectedItems():
        note_name = list_notes.selectedItems()[0].text() 
        notes[note_name]['текст'] = text_field.toPlainText()
        with open('notes.json','w',encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)

def note_delete():
    if list_notes.selectedItems():
        note_name = list_notes.selectedItems()[0].text() 

        del notes[note_name] 
        list_notes.clear()
        list_tags.clear()
        text_field.clear()

        list_notes.addItems(notes)
        with open('notes.json','w',encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)

def tag_create(): 
    if list_notes.selectedItems():
        note_name = list_notes.selectedItems()[0].text()
        tag = search_field.text()
        if tag != '' and tag not in notes[note_name]['теги']:
            notes[note_name]['теги'].append(tag)
            list_tags.addItem(tag)
        with open('notes.json','w',encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)

def tag_delete():
    if list_notes.selectedItems():
        note_name = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[note_name]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[note_name]['теги'])
        with open('notes.json','w',encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)
        
def search_notes():
    if search.text() == 'Поиск':
        tag = search_field.text()
        notes_filtred = {}
        for note_name in notes:
            if tag in notes[note_name]['теги']:
                notes_filtred[note_name] = notes[note_name]
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtred)
        search.setText('Сбросить')
    elif search.text() == 'Сбросить':
        list_notes.clear()
        list_tags.clear()
        search_field.clear()
        list_notes.addItems(notes)
        search.setText('Поиск')

# ПОДПИСКИ НА СОБЫТИЯ
list_notes.itemClicked.connect(show_note)
create_note.clicked.connect(note_create)
save_note.clicked.connect(note_save)
delete_note.clicked.connect(note_delete)
create_tag.clicked.connect(tag_create) 
delete_tag.clicked.connect(tag_delete) 
search.clicked.connect(search_notes) 
# ЗАПУСК

with open('notes.json','r',encoding='utf-8') as file:
    notes = json.load(file)


list_notes.addItems(notes)

window.setLayout(main_layout)
window.show()
app.exec()
