import os
import PyQt5

# Находим, где реально лежит PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
# Указываем путь к плагинам внутри библиотеки
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")
