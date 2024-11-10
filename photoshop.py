import os
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLabel,
    QFileDialog)

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Фотошоп')
window.resize(1600,800)

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

# РАЗМЕЩЕНИЕ
main_line = QHBoxLayout()
left_line = QVBoxLayout()
right_line = QVBoxLayout()
btn_line = QHBoxLayout()

main_line.addLayout(left_line, 20)
main_line.addLayout(right_line, 80)

left_line.addWidget(btn_folder)
left_line.addWidget(list_files)

right_line.addWidget(label_image)
right_line.addLayout(btn_line)

btn_line.addWidget(btn_left)
btn_line.addWidget(btn_right)
btn_line.addWidget(btn_mirror)
btn_line.addWidget(btn_sharp)
btn_line.addWidget(btn_bw)
btn_line.addWidget(btn_save)
btn_line.addWidget(btn_reset)

# СТИЛИЗАЦИЯ
window.setStyleSheet("""
    QWidget {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
    }
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        font-size: 18px;
        padding: 10px;
        margin: 5px;
        border: none;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #388e3c;
    }
    QListWidget {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 5px;
        font-size: 14px;
        color: #333;
    }
    QListWidget::item {
        padding: 8px;
    }
    QListWidget::item:selected {
        background-color: #2196F3;
        color: white;
    }
    QHBoxLayout, QVBoxLayout {
        margin: 0;
        padding: 10px;
    }
    QHBoxLayout {
        spacing: 15px;
    }
    QVBoxLayout {
        spacing: 10px;
    }
""")
# ФУНКЦИОНАЛ
workdir = ''

class ImageEditor():
    def __init__(self):
        self.image = None
        self.directory = None
        self.filename = None
        self.save_directory = 'mod/'

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(workdir,filename)
        self.image = Image.open(fullname)

    def show_image(self, path):
        pixmap_image = QPixmap(path)
        w, h = label_image.width(), label_image.height()
        pixmap_image = pixmap_image.scaled(w,h)
        label_image.setPixmap(pixmap_image)

    def save_image(self):
        path = os.path.join(workdir, self.save_directory)
        if not os.path.exists(path):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.save_image()
        path = os.path.join(workdir,self.save_directory,self.filename)
        self.show_image(path)

    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        path = os.path.join(workdir,self.save_directory,self.filename)
        self.show_image(path)

def show_images():
    global workdir
    list_files.clear()
    workdir = QFileDialog().getExistingDirectory()
    files = os.listdir(workdir)
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            list_files.addItem(file)

def show_chosen_image():
    if list_files.currentRow() >= 0 :
        filename = list_files.currentItem().text()
        work_image.load_image(filename)
        work_image.show_image( os.path.join(workdir, filename) )

# ПОДПИСКИ
work_image = ImageEditor()
list_files.currentRowChanged.connect(show_chosen_image)
btn_folder.clicked.connect(show_images)
btn_bw.clicked.connect(work_image.do_bw)
btn_mirror.clicked.connect(work_image.do_mirror)

# ЗАПУСК
window.setLayout(main_line)
window.show()
app.exec()
