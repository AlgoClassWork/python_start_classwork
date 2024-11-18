import os
from PIL import Image, ImageEnhance, ImageOps
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QListWidget, QLabel,
    QFileDialog)

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

# РАЗМЕЩЕНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА
main_line = QHBoxLayout()
left_line = QVBoxLayout()
right_line = QVBoxLayout()
buttons_line = QHBoxLayout()

main_line.addLayout(left_line, 20)
main_line.addLayout(right_line, 80)

left_line.addWidget(btn_folder)
left_line.addWidget(list_images)

right_line.addWidget(label_image)
right_line.addLayout(buttons_line)

buttons_line.addWidget(btn_left)
buttons_line.addWidget(btn_right)
buttons_line.addWidget(btn_mirror)
buttons_line.addWidget(btn_sharp)
buttons_line.addWidget(btn_bw)
buttons_line.addWidget(btn_save)
buttons_line.addWidget(btn_reset)

# СТИЛИЗАЦИЯ ИНТЕРФЕЙСА
window.setStyleSheet("""
    QWidget {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #2f2f2f;
        color: #f0f0f0;
    }
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 14px;
        border-radius: 5px;
        margin: 5px;
        min-width: 120px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #3e8e41;
    }
    QListWidget {
        background-color: #444;
        border-radius: 5px;
        padding: 10px;
        margin-top: 20px;
        color: #f0f0f0;
    }
    QListWidget::item {
        padding: 10px;
        border-bottom: 1px solid #555;
    }
    QListWidget::item:selected {
        background-color: #5a5a5a;
    }
    QHBoxLayout, QVBoxLayout {
        margin: 0;
        padding: 0;
    }
    QVBoxLayout {
        align-items: center;
    }
""")

# ФУНКЦИОНАЛ
def show_images():
    global directory
    directory = QFileDialog().getExistingDirectory()
    filenames = os.listdir(directory)
    list_images.clear()
    for file in filenames:
        if file.endswith('.jpg') or file.endswith('.png'):
            list_images.addItem(file)

def show_chosen_image():
    global image, fullname
    if list_images.currentRow() >= 0:
        filename = list_images.currentItem().text()
        fullname = os.path.join(directory, filename) 
        image = Image.open(fullname)
        pixmap_image = QPixmap(fullname).scaled(label_image.width(),label_image.height())
        label_image.setPixmap(pixmap_image)

def update_image():
    global image
    temp_path = 'temp_image.png'
    image.save(temp_path)
    pixmap_image = QPixmap(temp_path).scaled(label_image.width(),label_image.height())
    label_image.setPixmap(pixmap_image)
    os.remove(temp_path)

def do_left():
    global image
    image = image.rotate(90)
    update_image()

def do_right():
    global image
    image = image.rotate(-90)
    update_image()

def do_mirror():
    global image
    image = ImageOps.mirror(image)
    update_image()

def do_sharp():
    global image
    image = ImageEnhance.Sharpness(image).enhance(2)
    update_image()

def do_bw():
    global image
    image = image.convert('L')
    update_image()

def reset():
    global image
    image = Image.open(fullname)
    pixmap_image = QPixmap(fullname).scaled(label_image.width(),label_image.height())
    label_image.setPixmap(pixmap_image)

def save_image():
    global image
    directory = QFileDialog().getExistingDirectory()
    filename = list_images.currentItem().text()
    image.save(os.path.join(directory,filename))


# ПОДПИСКИ
btn_folder.clicked.connect(show_images)
list_images.currentRowChanged.connect(show_chosen_image)
btn_left.clicked.connect(do_left)
btn_right.clicked.connect(do_right)
btn_mirror.clicked.connect(do_mirror)
btn_sharp.clicked.connect(do_sharp)
btn_bw.clicked.connect(do_bw)
btn_reset.clicked.connect(reset)
btn_save.clicked.connect(save_image)

# ЗАПУСК ПРИЛОЖЕНИЯ
window.setWindowTitle('Фотожоб')
window.setLayout(main_line)
window.resize(1400, 800)
window.show()
app.exec()
