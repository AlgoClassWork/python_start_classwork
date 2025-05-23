import os
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QListWidget, QLabel,
    QHBoxLayout, QVBoxLayout,
    QFileDialog)

# Создание приложения и настройка главного окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Фотошоп на минималках')
window.setStyleSheet("""
    QWidget {
        background-color: #fafafa;
        color: #2c2c2c;
        font-family: 'Segoe UI', sans-serif;
        font-size: 15px;
    }

    QPushButton {
        background-color: #e3f2fd;
        border: 1px solid #90caf9;
        border-radius: 10px;
        padding: 10px 16px;
        min-width: 80px;
        font-weight: 500;
    }

    QPushButton:hover {
        background-color: #bbdefb;
    }

    QPushButton:pressed {
        background-color: #90caf9;
    }

    QListWidget {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 6px;
        padding: 6px;
    }

    QLabel {
        background-color: #ffffff;
        border: 2px solid #cfd8dc;
        border-radius: 12px;
        min-height: 350px;
        min-width: 500px;
        qproperty-alignment: AlignCenter;
        font-style: italic;
        color: #757575;
    }
""")
window.resize(1000, 650)

# Элементы интерфейса
btn_folder = QPushButton('📁 Папка')
list_files = QListWidget()

label_image = QLabel('Здесь будет картинка')

btn_left = QPushButton('⏪ Лево')
btn_right = QPushButton('⏩ Право')
btn_mirror = QPushButton('🔁 Зеркало')
btn_sharp = QPushButton('🌀 Резкость')
btn_gray = QPushButton('⚫ Ч/Б')

# Размещение элементов
line_main = QHBoxLayout()
line_v1 = QVBoxLayout()
line_v2 = QVBoxLayout()
line_btn = QHBoxLayout()

# Левый блок — 25% ширины
line_main.addLayout(line_v1, 25)
line_v1.addWidget(btn_folder)
line_v1.addWidget(list_files)

# Правый блок — 75% ширины
line_main.addLayout(line_v2, 75)
line_v2.addWidget(label_image)
line_v2.addSpacing(15)
line_v2.addLayout(line_btn)

# Кнопки снизу
for btn in [btn_left, btn_right, btn_mirror, btn_sharp, btn_gray]:
    btn.setFixedHeight(40)
    line_btn.addWidget(btn)

window.setLayout(line_main)
window.show()

# Функционал
def filter(files):
    images = []
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            images.append(file)
    return images

def get_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory() 

def show_files():
    get_workdir()
    filenames = filter( os.listdir(workdir) )
    list_files.addItems(filenames)

def show_chosen_image():
    filename = list_files.currentItem().text()
    image_worker.load_image(filename)
    image_worker.show_image( os.path.join( workdir, filename ) )

class ImageWorker:
    def __init__(self):
        self.image = None 
        self.dir = None 
        self.filename = None 
        self.save_dir = 'Mod/'

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def show_image(self, dir):
        image = QPixmap(dir).scaled(label_image.width(), label_image.height(), Qt.KeepAspectRatio)
        label_image.setPixmap(image)

    def save_image(self):
        dir = os.path.join(workdir, self.save_dir)
        if not os.path.exists(dir):
            os.mkdir(dir)

        fullname = os.path.join(dir, self.filename)
        self.image.save(fullname)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        dir = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(dir)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        dir = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(dir)
    

image_worker = ImageWorker()
# Подписки на события
list_files.currentRowChanged.connect(show_chosen_image)
btn_folder.clicked.connect(show_files)
btn_left.clicked.connect(image_worker.do_left)
btn_right.clicked.connect(image_worker.do_right)

# Запуск приложения
app.exec()
