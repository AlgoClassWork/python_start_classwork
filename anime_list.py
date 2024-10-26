from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QListWidget, QPushButton, QVBoxLayout
)

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('My Anime List')
text_field = QTextEdit()

anime_list = QListWidget()
create_anime = QPushButton('Добавить аниме')
delete_anime = QPushButton('Удалить аниме')
save_anime = QPushButton('Сохранить изменения')
# РАЗМЕЩЕНИЕ
main_line = QHBoxLayout()
main_line.addWidget(text_field)

list_line = QVBoxLayout()
main_line.addLayout(list_line)

list_line.addWidget(anime_list)
h1 = QHBoxLayout()
list_line.addLayout(h1)
h1.addWidget(create_anime)
h1.addWidget(delete_anime)
list_line.addWidget(save_anime)

window.setLayout(main_line)
# ЗАПУСК 
text_field.setText('Самое топовое оняме которое я смотрел')
window.show()
app.exec()
