import os
import PyQt5
# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

# Импорты
from PIL import Image, ImageFilter # pip install pillow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget,
    QLabel, QFileDialog
)

# Создание приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('Редактор')
window.resize(800, 600)

# Элементы интерфейса
button_folder = QPushButton('Папка')
list_images = QListWidget()

image_preview = QLabel('Предпросмотр изображения')
image_preview.setObjectName('image_preview')
button_left = QPushButton('Лево')
button_right = QPushButton('Право')
button_mirror = QPushButton('Зеркало')
button_sharp = QPushButton('Резкость')
button_gray = QPushButton('Ч | Б')

# Разметка
layout_main = QHBoxLayout()
layout_left = QVBoxLayout()
layout_right = QVBoxLayout()
layout_buttons = QHBoxLayout()

layout_main.addLayout(layout_left, 20)
layout_main.addLayout(layout_right, 80)
layout_right.addLayout(layout_buttons)

layout_left.addWidget(list_images)
layout_left.addWidget(button_folder)

layout_right.addWidget(image_preview)

layout_buttons.addWidget(button_left)
layout_buttons.addWidget(button_right)
layout_buttons.addWidget(button_mirror)
layout_buttons.addWidget(button_sharp)
layout_buttons.addWidget(button_gray)

# Глобальная стилизация через setStyleSheet
style = """
QWidget {
    background-color: #2b2b2b;
    color: #e6e6e6;
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 12px;
}
QListWidget {
    background-color: #1e1e1e;
    border: 1px solid #3c3c3c;
    padding: 6px;
}
QLabel#image_preview {
    background-color: #111111;
    border: 1px dashed #444444;
    min-width: 420px;
    min-height: 320px;
    qproperty-alignment: AlignCenter;
    padding: 8px;
}
QPushButton {
    background-color: #3a3a3a;
    border: 1px solid #5c5c5c;
    color: #ffffff;
    padding: 8px 12px;
    border-radius: 6px;
}
QPushButton:hover {
    background-color: #505050;
}
QPushButton:pressed {
    background-color: #2d6cff;
}
"""

app.setStyleSheet(style)

# Функционал приложения
def select_folder():
    global folder
    folder = QFileDialog.getExistingDirectory(window, 'Выбрать папку')
    if folder:
        list_images.clear()
        for file in os.listdir(folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                list_images.addItem(file)

def show_image(image_name):
    global image_path
    image_path = os.path.join(folder, image_name.text())
    image = QPixmap(image_path).scaled(image_preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    image_preview.setPixmap(image)

def rotate_left():
    image = Image.open(image_path)
    image = image.rotate(90, expand=True)
    image.save(image_path)
    show_image(list_images.currentItem())

def rotate_right():
    image = Image.open(image_path)
    image = image.rotate(270, expand=True)
    image.save(image_path)
    show_image(list_images.currentItem())

def apply_mirror():
    image = Image.open(image_path)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.save(image_path)
    show_image(list_images.currentItem())

def apply_sharp():
    image = Image.open(image_path)
    image = image.filter(ImageFilter.SHARPEN)
    image.save(image_path)
    show_image(list_images.currentItem())

def apply_gray():
    image = Image.open(image_path)
    image = image.convert('L')
    image.save(image_path)
    show_image(list_images.currentItem())

# Подписки на события
button_folder.clicked.connect(select_folder)
list_images.itemClicked.connect(show_image)

button_left.clicked.connect(rotate_left)
button_right.clicked.connect(rotate_right)
button_mirror.clicked.connect(apply_mirror)
button_sharp.clicked.connect(apply_sharp)
button_gray.clicked.connect(apply_gray)

# Запуск приложения
window.setLayout(layout_main)
window.show()
app.exec()
