from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QListWidget, QLabel,
    QHBoxLayout, QVBoxLayout )

# Создание приложения и настройка главного окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Фотошоп на минималках')
window.show()
# Создание элементов интерфейса
btn_folder = QPushButton('Папка')
list_files = QListWidget()

label_image = QLabel('Здесь будет картинка')

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Зеркало')
btn_sharp = QPushButton('Резкость')
btn_gray = QPushButton('Ч/Б')

# Размещение элементов интерфейса
line_main = QHBoxLayout()
line_v1 = QVBoxLayout()
line_v2 = QVBoxLayout()
line_btn = QHBoxLayout()

line_main.addLayout(line_v1, 20)
line_v1.addWidget(btn_folder)
line_v1.addWidget(list_files)

line_main.addLayout(line_v2, 80)
line_v2.addWidget(label_image)
line_v2.addLayout(line_btn)

line_btn.addWidget(btn_left)
line_btn.addWidget(btn_right)
line_btn.addWidget(btn_mirror)
line_btn.addWidget(btn_sharp)
line_btn.addWidget(btn_gray)

window.setLayout(line_main)
# Запуск приложения
app.exec()
