import os
import PyQt5
# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

# Импорты
from PIL import Image, ImageFilter # pip install pillow
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

# Элементы интерфейса
button_folder = QPushButton('Папка')
list_images = QListWidget()

image_preview = QLabel('Предпросмотр изображения')
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

layout_main.addLayout(layout_left)
layout_main.addLayout(layout_right)
layout_right.addLayout(layout_buttons)

layout_left.addWidget(list_images)
layout_left.addWidget(button_folder)

layout_right.addWidget(image_preview)

layout_buttons.addWidget(button_left)
layout_buttons.addWidget(button_right)
layout_buttons.addWidget(button_mirror)
layout_buttons.addWidget(button_sharp)
layout_buttons.addWidget(button_gray)

# Запуск приложения
window.setLayout(layout_main)
window.show()
app.exec()
