# шаг 1 импорты нужных технологий
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QListWidget, QLabel,
    QHBoxLayout, QVBoxLayout
)
# шаг 2 создаем пустое окно
app = QApplication([])
window = QWidget()
# создать левую часть интерфейса
folder_btn = QPushButton('Папка')
images_list = QListWidget()
# создать правую часть интерфейса
image_label = QLabel('Здесь будет картинка')
left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
mirror_btn = QPushButton('Зеркало')
sharp_btn = QPushButton('Резкость')
bw_btn = QPushButton('Ч\Б')
save_btn = QPushButton('Сохранить')
reset_btn = QPushButton('Сбросить')
 # создать линии
main_line = QHBoxLayout()
left_line = QVBoxLayout()
right_line = QVBoxLayout()
btn_line = QHBoxLayout()
# размещение нужных частей на главную линию
main_line.addLayout(left_line)
main_line.addLayout(right_line)
# размещение виджетов левой части интерфейса
left_line.addWidget(folder_btn)
left_line.addWidget(images_list)
# размещение виджетов правой части интерфейса
right_line.addWidget(image_label)
right_line.addLayout(btn_line)
# размещение кнопок на линию для кнопок
btn_line.addWidget(left_btn)
btn_line.addWidget(right_btn)
btn_line.addWidget(mirror_btn)
btn_line.addWidget(sharp_btn)
btn_line.addWidget(bw_btn)
btn_line.addWidget(save_btn)
btn_line.addWidget(reset_btn)
# разместить главную линию на экране
window.setLayout(main_line)
# запуск приложения
window.show()
app.exec()
