import os
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget

# Что бы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")


# Интерфейс
app = QApplication([])
window = QWidget()

window.show()
app.exec()
