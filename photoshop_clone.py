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

# Запуск приложения
window.show()
app.exec()
