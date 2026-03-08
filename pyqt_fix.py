import os
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

# Что бы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

# Интерфейс
app = QApplication([])
window = QWidget()
window.setWindowTitle("Генератор победителей")
text = QLabel("Нажмите на кнопку, чтобы сгенерировать победителя!")
winner = QLabel("Победитель: ")
button = QPushButton("Сгенерировать победителя")
# Размещение
layout = QVBoxLayout()
layout.addWidget(text)
layout.addWidget(winner)
layout.addWidget(button)
window.setLayout(layout)
# Запуск
window.show()
app.exec()
