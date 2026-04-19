import os
import PyQt5

pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

# =========================
# Импорты
# =========================
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QVBoxLayout,
    QHBoxLayout, QWidget, QLabel, QListWidget
)
from PyQt5.QtCore import Qt


# =========================
# Создание приложения
# =========================
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Редактор изображений')
main_window.resize(800, 500)


# =========================
# Элементы интерфейса
# =========================

# Левая панель
btn_select_folder = QPushButton('Выбрать папку')
list_images = QListWidget()

# Правая панель
label_preview = QLabel('Предпросмотр изображения')
label_preview.setAlignment(Qt.AlignCenter)

# Кнопки обработки
btn_rotate_left = QPushButton('⟲ Лево')
btn_rotate_right = QPushButton('⟳ Право')
btn_mirror = QPushButton('Зеркало')
btn_sharpness = QPushButton('Резкость')
btn_grayscale = QPushButton('Ч/Б')


# =========================
# Layout (разметка)
# =========================

# Главный layout
layout_main = QHBoxLayout()

# Левая колонка
layout_left = QVBoxLayout()
layout_left.addWidget(btn_select_folder)
layout_left.addWidget(list_images)

# Правая колонка
layout_right = QVBoxLayout()
layout_right.addWidget(label_preview)

# Нижние кнопки
layout_buttons = QHBoxLayout()
layout_buttons.addWidget(btn_rotate_left)
layout_buttons.addWidget(btn_rotate_right)
layout_buttons.addWidget(btn_mirror)
layout_buttons.addWidget(btn_sharpness)
layout_buttons.addWidget(btn_grayscale)

layout_right.addLayout(layout_buttons)

# Добавляем в главный layout
layout_main.addLayout(layout_left, 30)
layout_main.addLayout(layout_right, 70)

main_window.setLayout(layout_main)


# =========================
# Стили (минимальный UI)
# =========================
main_window.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
        color: #f0f0f0;
        font-size: 14px;
    }
    
    QPushButton {
        background-color: #3c3f41;
        border-radius: 6px;
        padding: 6px;
    }
    
    QPushButton:hover {
        background-color: #505354;
    }

    QListWidget {
        background-color: #1e1e1e;
        border: 1px solid #444;
    }

    QLabel {
        border: 1px solid #444;
        padding: 10px;
    }
""")


# =========================
# Запуск приложения
# =========================
main_window.show()
app.exec()
