import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QListWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QFileDialog)

# шаг 1: создаем приложение
app = QApplication([])

# шаг 2: создаем окно
window = QWidget()
window.setWindowTitle("Редактор изображений")

# шаг 3: создаем виджеты
folder_btn = QPushButton('Папка')
images_list = QListWidget()
image_label = QLabel('Здесь будет картинка')

left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
mirror_btn = QPushButton('Зеркало')
sharp_btn = QPushButton('Резкость')
bw_btn = QPushButton('Ч\Б')
save_btn = QPushButton('Сохранить')
reset_btn = QPushButton('Сбросить')

# шаг 4: создаем линии
main_line = QHBoxLayout()
left_line = QVBoxLayout()
right_line = QVBoxLayout()
btn_line = QHBoxLayout()

# шаг 5: размещение виджетов
main_line.addLayout(left_line, 20)
main_line.addLayout(right_line, 80)

# добавление виджетов в левую панель
left_line.addWidget(folder_btn)
left_line.addWidget(images_list)

# добавление виджетов в правую панель
right_line.addWidget(image_label)
right_line.addLayout(btn_line)

# добавление кнопок на панель с кнопками
btn_line.addWidget(left_btn)
btn_line.addWidget(right_btn)
btn_line.addWidget(mirror_btn)
btn_line.addWidget(sharp_btn)
btn_line.addWidget(bw_btn)
btn_line.addWidget(save_btn)
btn_line.addWidget(reset_btn)

# шаг 6: настраиваем стиль интерфейса с помощью CSS
window.setStyleSheet("""
    QWidget {
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f4;
    }
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 15px;
        font-size: 18px;
        margin: 5px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #397039;
    }
    QLabel {
        font-size: 18px;
        color: #333;
        background-color: #e2e2e2;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    }
    QListWidget {
        font-size: 14px;
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 5px;
    }
    QVBoxLayout, QHBoxLayout {
        spacing: 10px;
    }
    QHBoxLayout {
        margin-left: 20px;
        margin-right: 20px;
    }
""")
# Функционал
directory = ''
def show_images():
    images_list.clear()
    global directory
    directory = QFileDialog.getExistingDirectory()
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            images_list.addItem(file)

# Подписки
folder_btn.clicked.connect(show_images)
# Запуск
window.setLayout(main_line)
window.resize(1000, 600)
window.show()
app.exec()
