from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLabel)

# ИНТЕРФЕЙС
app = QApplication([])
window = QWidget()
window.setWindowTitle('Фотошоп')

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

main_line.addLayout(left_line,20)
main_line.addLayout(right_line,80)

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

# ЗАПУСК
window.setLayout(main_line)
window.show()
app.exec()
