import os
import PyQt5
# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton
# Создаем приложение и главное окно
app = QApplication([])
window = QWidget()
window.setWindowTitle("Конкурс")
window.setGeometry(1000, 500, 800, 600)
# Создаем виджеты для вопроса и вариантов ответов
question_label = QLabel("Вопрос: Какого цвета чернокожие?")
option_a = QRadioButton("А) Черные")
option_b = QRadioButton("Б) Белые")
option_c = QRadioButton("В) Зеленые")
option_d = QRadioButton("Г) Красные")
# Создаем вертикальный макет и добавляем виджеты
main_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
main_layout.addWidget(question_label)
main_layout.addLayout(h1_layout)
main_layout.addLayout(h2_layout)
h1_layout.addWidget(option_a)
h1_layout.addWidget(option_b)
h2_layout.addWidget(option_c)
h2_layout.addWidget(option_d)
window.setLayout(main_layout)
# Показываем окно и запускаем приложение
window.show()
app.exec()
