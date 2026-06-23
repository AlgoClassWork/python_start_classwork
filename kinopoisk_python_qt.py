import os
import PyQt5
# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")


from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QTextEdit, QListWidget,
    QPushButton, QLineEdit, 
    QVBoxLayout, QHBoxLayout,
    QInputDialog
)

# Создание интерфейса приложения
app = QApplication([])
window = QWidget()

description_field = QTextEdit()

film_list = QListWidget()
add_film_button = QPushButton("Добавить фильм")
del_film_button = QPushButton("Удалить фильм")

# Расположение элементов интерфейса
main_layout = QHBoxLayout()
list_layout = QVBoxLayout()
btn1_layout = QHBoxLayout()

main_layout.addWidget(description_field)

main_layout.addLayout(list_layout)

list_layout.addWidget(film_list)
list_layout.addLayout(btn1_layout)
btn1_layout.addWidget(add_film_button)
btn1_layout.addWidget(del_film_button)


window.setLayout(main_layout)
# Запуск приложения
window.show()
app.exec()
