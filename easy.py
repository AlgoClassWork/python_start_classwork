import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Диалог открытия файлов (и папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)

app = QApplication([])
window = QWidget()       
window.resize(700, 500) 
window.setWindowTitle('Easy Editor')
image_lable = QLabel("Картинка")
folder_button = QPushButton("Папка")
files_list = QListWidget()


left_button = QPushButton("Лево")
right_button = QPushButton("Право")
flip_button = QPushButton("Зеркало")
sharp_button = QPushButton("Резкость")
gray_button = QPushButton("Ч/Б")


main_line = QHBoxLayout()       
col1 = QVBoxLayout()         
col2 = QVBoxLayout()
col1.addWidget(folder_button)     
col1.addWidget(files_list)     
col2.addWidget(image_lable) 
row_buttons = QHBoxLayout()  
row_buttons.addWidget(left_button)
row_buttons.addWidget(right_button)
row_buttons.addWidget(flip_button)
row_buttons.addWidget(sharp_button)
row_buttons.addWidget(gray_button)
col2.addLayout(row_buttons)


main_line.addLayout(col1, 20)
main_line.addLayout(col2, 80)
window.setLayout(main_line)


# Функционал
def show_images():
   workdir = QFileDialog().getExistingDirectory()
   if workdir:
      files = os.listdir( workdir )
      files_list.clear()
      for file in files:
         if file.endswith('.jpg'):
            files_list.addItem(file)

# Подписки на события
folder_button.clicked.connect(show_images)

window.show()
app.exec()
