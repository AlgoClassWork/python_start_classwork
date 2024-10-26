from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QHBoxLayout,
    QListWidget, QPushButton , QVBoxLayout , QLineEdit
)
# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Фильмы')
text_field = QTextEdit()

list_films = QListWidget()
create_film = QPushButton('Добавить фильм')
delete_film = QPushButton('Удалить фильм')
save_film = QPushButton('Сохранить фильм')
# РАЗМЕЩЕНИЕ
main_line = QHBoxLayout()
main_line.addWidget(text_field)

list_line = QVBoxLayout()
main_line.addLayout(list_line)

list_line.addWidget(list_films)
list_line.addWidget(create_film)
list_line.addWidget(delete_film)
list_line.addWidget(save_film)

window.setLayout(main_line)
# ЗАПУСК
list_films.addItem('Великолепный век')
window.show()
app.exec()
