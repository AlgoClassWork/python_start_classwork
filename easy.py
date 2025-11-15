import os
from PIL import Image, ImageFilter, ImageOps
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

app = QApplication([])
window = QWidget()
window.resize(900, 550)
window.setWindowTitle('Easy Editor')

# ---------- СТИЛИ ОФОРМЛЕНИЯ ----------
app.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
        color: #f0f0f0;
        font-family: Segoe UI, Arial;
        font-size: 14px;
    }

    QLabel {
        background-color: #3c3c3c;
        qproperty-alignment: AlignCenter;
    }

    QListWidget {
        background-color: #3c3c3c;
        border: 2px solid #555;
        border-radius: 6px;
        padding: 4px;
    }

    QListWidget::item {
        padding: 6px;
    }

    QListWidget::item:selected {
        background-color: #5a97ff;
        color: white;
    }

    QPushButton {
        background-color: #4a4a4a;
        border: 1px solid #666;
        border-radius: 6px;
        padding: 6px 10px;
    }

    QPushButton:hover {
        background-color: #5c5c5c;
    }

    QPushButton:pressed {
        background-color: #6a6a6a;
    }

    QPushButton#saveButton {
        background-color: #2e7d32;
        border-color: #3fa844;
    }

    QPushButton#resetButton {
        background-color: #c62828;
        border-color: #ff5252;
    }
""")

# ---------- ЭЛЕМЕНТЫ ИНТЕРФЕЙСА ----------

image_lable = QLabel("Картинка")
folder_button = QPushButton("Папка")
files_list = QListWidget()

# Кнопки фильтров
left_button = QPushButton("Лево")
right_button = QPushButton("Право")
flip_button = QPushButton("Зеркало")
sharp_button = QPushButton("Резкость")
gray_button = QPushButton("Ч/Б")

blur_button = QPushButton("Размытие")
contour_button = QPushButton("Контур")
detail_button = QPushButton("Детализация")
emboss_button = QPushButton("Тиснение")
edges_button = QPushButton("Края")
smooth_button = QPushButton("Сглаживание")
invert_button = QPushButton("Инверсия")

save_button = QPushButton("Сохранить как...")
reset_button = QPushButton("Сбросить")

# Имена для стилевого оформления
save_button.setObjectName("saveButton")
reset_button.setObjectName("resetButton")

# Основная раскладка
main_line = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(folder_button)
col1.addWidget(files_list)

col2.addWidget(image_lable)

row1 = QHBoxLayout()
row1.addWidget(left_button)
row1.addWidget(right_button)
row1.addWidget(flip_button)
row1.addWidget(sharp_button)
row1.addWidget(gray_button)

row2 = QHBoxLayout()
row2.addWidget(blur_button)
row2.addWidget(contour_button)
row2.addWidget(detail_button)
row2.addWidget(emboss_button)

row3 = QHBoxLayout()
row3.addWidget(edges_button)
row3.addWidget(smooth_button)
row3.addWidget(invert_button)

row4 = QHBoxLayout()
row4.addWidget(save_button)
row4.addWidget(reset_button)

col2.addLayout(row1)
col2.addLayout(row2)
col2.addLayout(row3)
col2.addLayout(row4)

main_line.addLayout(col1, 20)
main_line.addLayout(col2, 80)
window.setLayout(main_line)

# ─────────────────────────────────────────────
#            ФУНКЦИОНАЛ РЕДАКТОРА
# ─────────────────────────────────────────────
class ImageEditor():
    def __init__(self):
        self.image = None
        self.original = None
        self.dir = None
        self.filename = None
        self.path = None

    def load_image(self, dir, filename):
        self.dir = dir
        self.filename = filename
        self.path = os.path.join(dir, filename)
        self.image = Image.open(self.path)
        self.original = self.image.copy()

    def show_image(self):
        image = QPixmap(self.path)
        image = image.scaled(image_lable.width(), image_lable.height(), Qt.KeepAspectRatio)
        image_lable.setPixmap(image)

    def save_temp(self):
        temp_path = os.path.join(os.getcwd(), "temp_edit.jpg")
        self.image.save(temp_path)
        self.path = temp_path

    def save_as(self):
        if self.image:
            save_path, _ = QFileDialog.getSaveFileName(window, "Сохранить изображение", "", "*.jpg")
            if save_path:
                self.image.save(save_path)

    def reset(self):
        if self.image:
            self.image = self.original.copy()
            self.save_temp()
            self.show_image()

    # Базовые фильтры
    def left_filter(self):
        if self.image:
            self.image = self.image.transpose(Image.ROTATE_90)
            self.save_temp()
            self.show_image()

    def right_filter(self):
        if self.image:
            self.image = self.image.transpose(Image.ROTATE_270)
            self.save_temp()
            self.show_image()

    def flip_filter(self):
        if self.image:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.save_temp()
            self.show_image()

    def sharp_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.save_temp()
            self.show_image()

    def gray_filter(self):
        if self.image:
            self.image = self.image.convert('L')
            self.save_temp()
            self.show_image()

    # Новые фильтры
    def blur_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.save_temp()
            self.show_image()

    def contour_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.CONTOUR)
            self.save_temp()
            self.show_image()

    def detail_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.DETAIL)
            self.save_temp()
            self.show_image()

    def emboss_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.EMBOSS)
            self.save_temp()
            self.show_image()

    def edges_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.FIND_EDGES)
            self.save_temp()
            self.show_image()

    def smooth_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.SMOOTH)
            self.save_temp()
            self.show_image()

    def invert_filter(self):
        if self.image:
            self.image = ImageOps.invert(self.image.convert("RGB"))
            self.save_temp()
            self.show_image()

# ─────────────────────────────────────────────
#               ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ─────────────────────────────────────────────

def show_files():
    global workdir
    workdir = QFileDialog().getExistingDirectory()
    if workdir:
        files = os.listdir(workdir)
        files_list.clear()
        for file in files:
            if file.lower().endswith(('.jpg', '.png', '.jpeg', '.bmp')):
                files_list.addItem(file)

def show_chosen_image():
    filename = files_list.currentItem().text()
    image_editor.load_image(workdir, filename)
    image_editor.show_image()

# ─────────────────────────────────────────────
#                  ПОДПИСКИ
# ─────────────────────────────────────────────

image_editor = ImageEditor()

files_list.itemClicked.connect(show_chosen_image)
folder_button.clicked.connect(show_files)

left_button.clicked.connect(image_editor.left_filter)
right_button.clicked.connect(image_editor.right_filter)
flip_button.clicked.connect(image_editor.flip_filter)
sharp_button.clicked.connect(image_editor.sharp_filter)
gray_button.clicked.connect(image_editor.gray_filter)

blur_button.clicked.connect(image_editor.blur_filter)
contour_button.clicked.connect(image_editor.contour_filter)
detail_button.clicked.connect(image_editor.detail_filter)
emboss_button.clicked.connect(image_editor.emboss_filter)
edges_button.clicked.connect(image_editor.edges_filter)
smooth_button.clicked.connect(image_editor.smooth_filter)
invert_button.clicked.connect(image_editor.invert_filter)

save_button.clicked.connect(image_editor.save_as)
reset_button.clicked.connect(image_editor.reset)

window.show()
app.exec()
