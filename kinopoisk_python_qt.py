import os
import PyQt5
# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")


from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QTextEdit, QListWidget,
    QPushButton, QLineEdit, 
    QVBoxLayout, QHBoxLayout,
    QInputDialog
)

# Создание интерфейса приложения
app = QApplication([])
window = QWidget()

# Запуск приложения
window.show()
app.exec()
