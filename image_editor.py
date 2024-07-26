from PyQt5.QtWidgets import (
    QPushButton, QListWidget, QLabel,
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout)

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.resize(1000,600)
window.setWindowTitle('Photoshop')

btn_folder = QPushButton('Папка')
list_images = QListWidget()

image_field = QLabel('Здесь будет картинка!')

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Зеркало')
btn_sharpen = QPushButton('Резкость')
btn_gray = QPushButton('Ч\Б')

# ЗАПУСК
window.show()
app.exec()
