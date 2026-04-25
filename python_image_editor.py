import os
import PyQt5

pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

# =========================
# Импорты
# =========================
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QVBoxLayout,
    QHBoxLayout, QWidget, QLabel, QListWidget, QFileDialog)



# =========================
# Создание приложения
# =========================
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Редактор изображений')
main_window.resize(800, 500)


# =========================
# Элементы интерфейса
# =========================

# Левая панель
btn_select_folder = QPushButton('Выбрать папку')
list_images = QListWidget()

# Правая панель
label_preview = QLabel('Предпросмотр изображения')
label_preview.setAlignment(Qt.AlignCenter)

# Кнопки обработки
btn_rotate_left = QPushButton('⟲ Лево')
btn_rotate_right = QPushButton('⟳ Право')
btn_mirror = QPushButton('Зеркало')
btn_sharpness = QPushButton('Резкость')
btn_grayscale = QPushButton('Ч/Б')


# =========================
# Layout (разметка)
# =========================

# Главный layout
layout_main = QHBoxLayout()

# Левая колонка
layout_left = QVBoxLayout()
layout_left.addWidget(btn_select_folder)
layout_left.addWidget(list_images)

# Правая колонка
layout_right = QVBoxLayout()
layout_right.addWidget(label_preview)

# Нижние кнопки
layout_buttons = QHBoxLayout()
layout_buttons.addWidget(btn_rotate_left)
layout_buttons.addWidget(btn_rotate_right)
layout_buttons.addWidget(btn_mirror)
layout_buttons.addWidget(btn_sharpness)
layout_buttons.addWidget(btn_grayscale)

layout_right.addLayout(layout_buttons)

# Добавляем в главный layout
layout_main.addLayout(layout_left, 30)
layout_main.addLayout(layout_right, 70)

main_window.setLayout(layout_main)


# =========================
# Стили (минимальный UI)
# =========================
main_window.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
        color: #f0f0f0;
        font-size: 14px;
    }
    
    QPushButton {
        background-color: #3c3f41;
        border-radius: 6px;
        padding: 6px;
    }
    
    QPushButton:hover {
        background-color: #505354;
    }

    QListWidget {
        background-color: #1e1e1e;
        border: 1px solid #444;
    }
""")

# =========================
# Функционал
# =========================
def select_folder():
    global folder
    folder = QFileDialog.getExistingDirectory(main_window, "Выберите папку с изображениями")
    if folder:
        list_images.clear()
        for file in os.listdir(folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                list_images.addItem(file)

def show_image(item):
    global image_path
    image_path = os.path.join(folder, item.text())
    pixmap = QPixmap(image_path)
    label_preview.setPixmap(pixmap.scaled(label_preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

def rotate_left():
    if image_path:
        img = Image.open(image_path)
        img = img.rotate(90, expand=True)
        img.save(image_path)
        show_image(list_images.currentItem())

def rotate_right():
    if image_path:
        img = Image.open(image_path)
        img = img.rotate(270, expand=True)
        img.save(image_path)
        show_image(list_images.currentItem())

def mirror_image():
    if image_path:
        img = Image.open(image_path)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save(image_path)
        show_image(list_images.currentItem())

def apply_sharpness():
    if image_path:
        img = Image.open(image_path)
        img = img.filter(ImageFilter.SHARPEN)
        img.save(image_path)
        show_image(list_images.currentItem())

def apply_grayscale():
    if image_path:
        img = Image.open(image_path)
        img = img.convert('L')
        img.save(image_path)
        show_image(list_images.currentItem())

# =========================
# Подписки на события
# =========================
list_images.itemClicked.connect(show_image)
btn_select_folder.clicked.connect(select_folder)

btn_rotate_left.clicked.connect(rotate_left)
btn_rotate_right.clicked.connect(rotate_right)
btn_mirror.clicked.connect(mirror_image)
btn_sharpness.clicked.connect(apply_sharpness)
btn_grayscale.clicked.connect(apply_grayscale)

# =========================
# Запуск приложения
# =========================
main_window.show()
app.exec()
