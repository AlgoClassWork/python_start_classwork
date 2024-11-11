from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout,QVBoxLayout,
    QPushButton, QListWidget, QLabel)

# СОЗДАЕМ ЭЛЕМЕНТЫ ИНТЕРФЕЙСА
app = QApplication([])
window = QWidget()

btn_folder = QPushButton('Папка')
list_images = QListWidget()

label_image = QLabel('Картинка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Отзеркалить')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч\Б')
btn_save = QPushButton('Сохранить')
btn_reset = QPushButton('Сбросить')

# ЗАПУСК ПРИЛОЖЕНИЯ
window.show()
app.exec()
