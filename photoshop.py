from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLabel)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Фотошоп')

btn_folder = QPushButton('Папка')
list_files = QListWidget()

label_image = QLabel('Это картинка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Зеркало')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч\Б')
btn_save = QPushButton('Сохранить')
btn_reset = QPushButton('Сбросить')

window.show()
app.exec()
