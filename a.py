# шаг 1 импорты нужных технологий
# шаг 2 создаем пустое окно
# шаг 3 создаем нужные обьекты (виджеты)
    # создать левую часть интерфейса
    # создать правую часть интерфейса
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QListWidget, QLabel,
    QHBoxLayout, QVBoxLayout
)
# шаг 2 создаем пустое окно
app = QApplication([])
window = QWidget()

folder_btn = QPushButton('Папка')
images_list = QListWidget()

image_label = QLabel('Здесь будет картинка')
left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
mirror_btn = QPushButton('Зеркало')
sharp_btn = QPushButton('Резкость')
bw_btn = QPushButton('Ч\Б')
save_btn = QPushButton('Сохранить')
reset_btn = QPushButton('Сбросить')


window.show()
app.exec()
