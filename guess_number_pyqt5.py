import os
import PyQt5

pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")


#pip install pyqt5
from PyQt5.QtWidgets import (
QApplication, QWidget, QVBoxLayout,
QPushButton, QLabel, QLineEdit )

app = QApplication([])
window = QWidget()

label = QLabel("Угадай число от 1 до 100")
input_field = QLineEdit()
button = QPushButton("Проверить")

layout = QVBoxLayout()
window.setLayout(layout)
layout.addWidget(label)
layout.addWidget(input_field)
layout.addWidget(button)

window.show()
app.exec()
