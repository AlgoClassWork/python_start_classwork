import os
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout)

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
class ImageEditor():
   def __init__(self):
      self.image = None 
      self.dir = None 
      self.filename = None
      self.path = None

   def load_image(self, dir, filename):
      self.dir = dir # c:/Users/Kyxec/Desktop/easy/
      self.filename = filename # cat.jpg
      self.path = os.path.join(dir, filename) # c:/Users/Kyxec/Desktop/easy/cat.jpg
      self.image = Image.open( self.path )

   def show_image(self):
      image = QPixmap(self.path)
      image = image.scaled(image_lable.width(), image_lable.height(), Qt.KeepAspectRatio)
      image_lable.setPixmap(image)

   def save_image(self):
      current_dir = os.getcwd()
      path = os.path.join(current_dir, 'mod')
      if not ( os.path.exists(path) or os.path.isdir(path) ) :
         os.mkdir(path)
      self.path = os.path.join(path, self.filename)
      self.image.save(self.path)

   def left_filter(self):
      self.image = self.image.transpose(Image.ROTATE_90)
      self.save_image()
      self.show_image()

   def right_filter(self):
      self.image = self.image.transpose(Image.ROTATE_270)
      self.save_image()
      self.show_image()

   def flip_filter(self):
      self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
      self.save_image()
      self.show_image()

   def sharp_filter(self):
      self.image = self.image.filter(ImageFilter.SHARPEN)
      self.save_image()
      self.show_image()

   def gray_filter(self):
      self.image = self.image.convert('L')
      self.save_image()
      self.show_image()

def show_files():
   global workdir
   workdir = QFileDialog().getExistingDirectory()
   if workdir:
      files = os.listdir( workdir )
      files_list.clear()
      for file in files:
         if file.endswith('.jpg'):
            files_list.addItem(file)

def show_chosen_image():
   filename = files_list.currentItem().text()
   image_editor.load_image( workdir, filename)
   image_editor.show_image()

# Подписки на события
image_editor = ImageEditor()

files_list.itemClicked.connect(show_chosen_image)
folder_button.clicked.connect(show_files)

left_button.clicked.connect(image_editor.left_filter)
right_button.clicked.connect(image_editor.right_filter)
flip_button.clicked.connect(image_editor.flip_filter)
sharp_button.clicked.connect(image_editor.sharp_filter)
gray_button.clicked.connect(image_editor.gray_filter)


window.show()
app.exec()
