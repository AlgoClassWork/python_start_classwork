from PyQt5.QtWidgets import (
    QApplication, QPushButton, QVBoxLayout,
    QHBoxLayout, QWidget, QLabel, QListWidget
)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Редактор изображений')

folder_button = QPushButton('Выбрать папку')
image_list = QListWidget()

preview_label = QLabel('Предпросмотр изображения')

left_button = QPushButton('Лево')
right_button = QPushButton('Право')
mirror_button = QPushButton('Зеркало')
sharpness_button = QPushButton('Резкость')
gray_button = QPushButton('Черно-белое')


main_layout = QHBoxLayout()
v1_layout = QVBoxLayout()
v2_layout = QVBoxLayout()
buttons_layout = QHBoxLayout()

main_layout.addLayout(v1_layout)
main_layout.addLayout(v2_layout)

v1_layout.addWidget(folder_button)
v1_layout.addWidget(image_list)

v2_layout.addWidget(preview_label)
v2_layout.addLayout(buttons_layout)

buttons_layout.addWidget(left_button)
buttons_layout.addWidget(right_button)
buttons_layout.addWidget(mirror_button)
buttons_layout.addWidget(sharpness_button)
buttons_layout.addWidget(gray_button)

window.setLayout(main_layout)

window.show()
app.exec()
