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
window.setWindowTitle("Квиз")
window.resize(400, 300) # Немного увеличим стартовый размер для красоты

question_label = QLabel("Почему небо голубое?")

answer_group = QGroupBox("Выберите ответ:")

answer_rbtn1 = QRadioButton("Из-за рассеяния света в атмосфере")
answer_rbtn2 = QRadioButton("Из-за отражения океанов")
answer_rbtn3 = QRadioButton("Из-за наличия кислорода в воздухе")
answer_rbtn4 = QRadioButton("Из-за солнечных лучей")

result_group = QGroupBox("Результат:")
result_label = QLabel("")

ok_button = QPushButton("Проверить ответ")

# Размещение виджетов
main_layout = QVBoxLayout()
answer_layout = QVBoxLayout()
result_layout = QVBoxLayout()

main_layout.addWidget(question_label)
main_layout.addWidget(answer_group)
main_layout.addWidget(result_group)

answer_layout.addWidget(answer_rbtn1)
answer_layout.addWidget(answer_rbtn2)
answer_layout.addWidget(answer_rbtn3)
answer_layout.addWidget(answer_rbtn4)

result_layout.addWidget(result_label)

main_layout.addWidget(ok_button)

answer_group.setLayout(answer_layout)
result_group.setLayout(result_layout)
window.setLayout(main_layout)

# --- Стилизация приложения ---
style_sheet = """
    /* Общий стиль для главного окна */
    QWidget {
        background-color: #1e1e24;
        color: #f5f5f7;
        font-family: "Segoe UI", sans-serif;
        font-size: 14px;
    }

    /* Стиль для вопроса */
    QLabel {
        font-size: 18px;
        font-weight: bold;
        color: #00adb5;
        padding: 10px 0px;
    }

    /* Стиль для контейнера ответов */
    QGroupBox {
        font-weight: bold;
        color: #eeeeee;
        border: 2px solid #393e46;
        border-radius: 8px;
        margin-top: 15px;
        padding-top: 15px;
    }
    
    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top left;
        left: 15px;
        padding: 0 5px;
    }

    /* Стиль для радио-кнопок (вариантов ответа) */
    QRadioButton {
        padding: 6px;
        spacing: 10px;
    }
    
    QRadioButton::indicator {
        width: 16px;
        height: 16px;
        border-radius: 9px;
        border: 2px solid #393e46;
        background-color: #222831;
    }

    QRadioButton::indicator:hover {
        border-color: #00adb5;
    }

    QRadioButton::indicator:checked {
        background-color: #00adb5;
        border: 2px solid #eeeeee;
    }

    /* Стиль для главной кнопки */
    QPushButton {
        background-color: #00adb5;
        color: #eeeeee;
        font-weight: bold;
        border: none;
        border-radius: 6px;
        padding: 10px 20px;
        margin-top: 15px;
    }

    QPushButton:hover {
        background-color: #00c2cb;
    }

    QPushButton:pressed {
        background-color: #008c94;
    }
"""

app.setStyleSheet(style_sheet)
# -----------------------------

# Запуск приложения
window.show()
app.exec()
