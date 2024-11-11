from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout,QVBoxLayout,
    QPushButton, QListWidget, QLabel)

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

# ЗАПУСК ПРИЛОЖЕНИЯ
window.setWindowTitle('Фотожоб')
window.setLayout(main_line)
window.resize(800,500)
window.show()
app.exec()
