from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLabel)

#СОЗДАНИЕ ИНТЕРФЕЙСА
app = QApplication([])
window = QWidget()
window.resize(700,500)
window.setWindowTitle('Фотошоп на минималках')

folder = QPushButton('Папка')
files = QListWidget()

image = QLabel('Картинка')
left = QPushButton('Лево')
right = QPushButton('Право')
flip = QPushButton('Зеркало')
sharp = QPushButton('Резкость')
gray = QPushButton('Ч\Б')
# ЗАПУСК
window.show()
app.exec()
