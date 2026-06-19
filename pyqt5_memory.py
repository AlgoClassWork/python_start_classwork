import os
import PyQt5
# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

# Наше приложение
# pip install pyqt5
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QGroupBox, QRadioButton, QPushButton,
    QVBoxLayout, QHBoxLayout
)

# Создание интерфейса
app = QApplication([])
window = QWidget()

question_label = QLabel("Почему небо голубое?")

answer_group = QGroupBox("Выберите ответ:")
answer_rbtn1 = QRadioButton("Из-за рассеяния света в атмосфере")

# Размещение виджетов
main_layout = QVBoxLayout()
answer_layout = QVBoxLayout()

main_layout.addWidget(question_label)
main_layout.addWidget(answer_group)
answer_layout.addWidget(answer_rbtn1)

answer_group.setLayout(answer_layout)
window.setLayout(main_layout)

# Запуск приложения
window.show()
app.exec()
