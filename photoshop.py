import os
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLabel, QFileDialog)

# Интерфейс приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('Фотошоп на минималках')
window.resize(800,400)

# Устанавливаем общий стиль для всего приложения в светлых тонах
window.setStyleSheet("""
    QWidget {
        background-color: lightgray; /* Очень светло-серый фон */
        color: black; /* Темный текст для контраста */
        font-family: 'Segoe UI', sans-serif;
        font-size: 15px;
    }
    QPushButton {
        background-color: lightblue; /* Светло-серый фон кнопок */
        border: 1px solid black; /* Более светлая рамка */
        border-radius: 5px; /* Скругленные углы */
        padding: 10px 15px; /* Отступы внутри кнопки */
        color: black; /* Темный текст кнопок */
        font-weight: bold;
    }
    QListWidget {
        background-color: white; /* Белый фон списка */
        border: 1px solid black; /* Светлая рамка */
        border-radius: 5px;
        padding: 5px;
        color: black; /* Темный текст списка */
    }
    QListWidget::item {
        padding: 5px;
    }
    QListWidget::item:selected {
        background-color: lightblue; /* Светло-голубой фон для выбранных элементов */
        color: black;
    }
    QLabel {
        color: black; /* Темный текст для меток */
        background-color: white; /* Очень светлый фон для области изображения */
        border: 1px solid black;
        qproperty-alignment: AlignCenter; /* Выравнивание содержимого по центру */
        font-weight: bold;
    }
""")


folder_btn = QPushButton('Папка')
files_list = QListWidget()

image_lbl = QLabel('Картинка')
image_lbl.setFixedSize(image_lbl.width() - 50, image_lbl.height() - 100)

left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
flip_btn = QPushButton('Зеркало')
sharpen_btn = QPushButton('Резкость')
gray_btn = QPushButton('Ч/Б')

# Размещение
main_line = QHBoxLayout()
v1_line = QVBoxLayout()
v2_line = QVBoxLayout()
btns_line = QHBoxLayout()

v1_line.addWidget(folder_btn)
v1_line.addWidget(files_list)
v2_line.addWidget(image_lbl)

btns_line.addWidget(left_btn)
btns_line.addWidget(right_btn)
btns_line.addWidget(flip_btn)
btns_line.addWidget(sharpen_btn)
btns_line.addWidget(gray_btn)

main_line.addLayout(v1_line, 30)
main_line.addLayout(v2_line, 70)
v2_line.addLayout(btns_line)

window.setLayout(main_line)

# Функционал
class ImageWorker():
    def __init__(self):
        self.image = None
        self.directory = None
        self.filename = None
        self.save_directory = 'Mod/'

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(directory, filename)
        self.image = Image.open(fullname)

    def show_image(self, fullname):
        image = QPixmap(fullname)
        width, height = image_lbl.width(), image_lbl.height()
        image = image.scaled(width, height, Qt.KeepAspectRatio)
        image_lbl.setPixmap( image )

    def save_image(self):
        save_directory = os.path.join( directory, self.save_directory )
        if not os.path.exists(save_directory):
            os.mkdir(save_directory)
        self.image.save( os.path.join(save_directory, self.filename) )

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        self.show_image(os.path.join(directory, self.save_directory, self.filename))

def show_files():
    global directory
    directory = QFileDialog.getExistingDirectory() 
    print(directory)
    filenames = os.listdir(directory) 
    for file in filenames:
        if file.endswith('.jpg') or file.endswith('.png'):
            files_list.addItem(file)

def show_chosen_image():
    filename = files_list.currentItem().text() 
    image_worker.load_image(filename)
    image_worker.show_image( os.path.join(directory, filename) )

# Подписки на события
image_worker = ImageWorker()

files_list.itemClicked.connect(show_chosen_image)
folder_btn.clicked.connect(show_files)
left_btn.clicked.connect(image_worker.do_left)
# Запуск приложения
window.show()
app.exec()
