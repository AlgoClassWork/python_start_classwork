import os
from random import randint
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

# Твой фикс для платформы
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

app = QApplication([])
window = QWidget()

# --- Только стилизация ---
window.setWindowTitle("Угадай число")
window.setFixedSize(320, 200)

window.setStyleSheet("""
    QWidget {
        background-color: #1e1e2e;
        font-family: 'Segoe UI', sans-serif;
    }
    QLabel {
        color: #cdd6f4;
        font-size: 16px;
        font-weight: bold;
        qproperty-alignment: AlignCenter;
    }
    QLineEdit {
        background-color: #313244;
        color: #a6e3a1;
        border: 2px solid #45475a;
        border-radius: 6px;
        padding: 6px;
        font-size: 15px;
        qproperty-alignment: AlignCenter;
    }
    QLineEdit:focus {
        border: 2px solid #cba6f7;
    }
    QPushButton {
        background-color: #89b4fa;
        color: #11111b;
        border-radius: 6px;
        padding: 8px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #b4befe;
    }
    QPushButton:pressed {
        background-color: #74c7ec;
    }
""")
# -------------------------

label = QLabel("Угадай число от 1 до 100")
input_field = QLineEdit()
button = QPushButton("Угадать")

layout = QVBoxLayout()
layout.setSpacing(12)  # Небольшой отступ между элементами
window.setLayout(layout)
layout.addWidget(label)
layout.addWidget(input_field)
layout.addWidget(button)

window.show()
app.exec()
