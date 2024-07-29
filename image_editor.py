import os
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton, QListWidget, QLabel,
    QApplication, QWidget, QFileDialog,
    QVBoxLayout, QHBoxLayout)

styles = """
QWidget {
    background-color: #f0f0f0; /* Светлый фон для всего окна */
}

QPushButton {
    background-color: #007BFF; /* Основной цвет кнопок */
    color: white; /* Цвет текста кнопок */
    border: 2px solid #0056b3; /* Цвет рамки кнопок */
    border-radius: 5px; /* Скругление углов кнопок */
    padding: 10px; /* Отступы внутри кнопок */
    font-size: 14px; /* Размер шрифта кнопок */
}

QPushButton:hover {
    background-color: #0056b3; /* Цвет кнопок при наведении */
}

QPushButton:pressed {
    background-color: #003d7a; /* Цвет кнопок при нажатии */
}

QListWidget {
    background-color: #ffffff; /* Фон для списка изображений */
    border: 2px solid #007BFF; /* Рамка списка изображений */
    border-radius: 5px; /* Скругление углов списка изображений */
    padding: 10px; /* Отступы внутри списка изображений */
}

QLabel {
    background-color: #ffffff; /* Фон для метки с изображением */
    border: 2px solid #007BFF; /* Рамка метки */
    border-radius: 5px; /* Скругление углов метки */
    padding: 10px; /* Отступы внутри метки */
    font-size: 16px; /* Размер шрифта метки */
    color: #333333; /* Цвет текста метки */
}
"""

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.resize(700,500)
window.setWindowTitle('Photoshop')
window.setStyleSheet(styles)

btn_folder = QPushButton('Папка')
list_images = QListWidget()

image_field = QLabel('Здесь будет картинка!')

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Зеркало')
btn_sharpen = QPushButton('Резкость')
btn_gray = QPushButton('Ч\Б')

# РАСПОЛОЖЕНИЕ
main_line = QHBoxLayout()

v1_line = QVBoxLayout()
v1_line.addWidget(btn_folder)
v1_line.addWidget(list_images)
main_line.addLayout(v1_line, stretch=20)

h_line = QHBoxLayout()
h_line.addWidget(btn_left)
h_line.addWidget(btn_right)
h_line.addWidget(btn_mirror)
h_line.addWidget(btn_sharpen)
h_line.addWidget(btn_gray)

v2_line = QVBoxLayout()
v2_line.addWidget(image_field)
v2_line.addLayout(h_line)
main_line.addLayout(v2_line, stretch=80)

window.setLayout(main_line)
# ФУНКЦИОНАЛ
put_k_papke = ''
tekushiya_kartinka = '' 
imya_faila = ''
polnyi_put = ''

def show_images():
    global put_k_papke
    put_k_papke = QFileDialog.getExistingDirectory()
    filenames = os.listdir(put_k_papke)
    for file in filenames:
        if file.endswith('.jpeg') or file.endswith('.png'):
            list_images.addItem(file)

def show_chosen_image():
    global tekushiya_kartinka , polnyi_put, imya_faila
    imya_faila = list_images.currentItem().text()
    polnyi_put = os.path.join(put_k_papke,imya_faila)
    # показ изображения
    tekushiya_kartinka = Image.open(polnyi_put)
    kartinka_na_ekran = QPixmap(polnyi_put).scaled(image_field.width(),image_field.height(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
    image_field.setPixmap(kartinka_na_ekran)
    image_field.setFixedSize(image_field.width(),image_field.height())

def do_gray():
    global tekushiya_kartinka
    tekushiya_kartinka = tekushiya_kartinka.convert('L')
    put_sohraneniya = os.path.join(put_k_papke,'Mod/')
    if not os.path.exists(put_sohraneniya):
        os.mkdir(put_sohraneniya)
    put_k_mod_kartinke = os.path.join(put_sohraneniya,imya_faila)
    tekushiya_kartinka.save(put_k_mod_kartinke)

    kartinka_na_ekran = QPixmap(put_k_mod_kartinke).scaled(image_field.width(),image_field.height(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
    image_field.setPixmap(kartinka_na_ekran)
    image_field.setFixedSize(image_field.width(),image_field.height())
    
# ПОДПИСКИ
list_images.currentRowChanged.connect(show_chosen_image)
btn_folder.clicked.connect(show_images)
btn_gray.clicked.connect(do_gray)
# ЗАПУСК
window.show()
app.exec()
