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
    QVBoxLayout
)

# База данных вопросов и ответов
class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = [
    Question(
        "Какое животное способно пережить экстремальные температуры, радиацию и даже вакуум космоса?",
        "Тихоходка",
        "Таракан",
        "Скорпион",
        "Глубоководный кальмар"
    ),
    Question(
        "Какая планета Солнечной системы является самой горячей?",
        "Венера",
        "Меркурий",
        "Марс",
        "Юпитер"
    ),
    Question(
        "Какое культовое изобретение изначально создавалось как средство от головной боли и нервных расстройств?",
        "Кока-Кола",
        "Динамит",
        "Чайный пакетик",
        "Микроволновая печь"
    ),
    Question(
        "Какая страна является абсолютным лидером по количеству часовых поясов на своей территории (включая заморские владения)?",
        "Франция",
        "Россия",
        "США",
        "Канада"
    ),
    Question(
        "Что из этого является самым большим живым организмом на Земле?",
        "Опёнок тёмный (грибница в Орегоне)",
        "Синий кит",
        "Секвойя «Генерал Шерман»",
        "Большой Барьерный риф"
    ),
    Question(
        "Какое человеческое чувство первым просыпается после сна и последним «отключается» при засыпании?",
        "Слух",
        "Осязание",
        "Обоняние",
        "Зрение"
    ),
    Question(
        "Какое животное изображено на логотипе популярного языка программирования Python?",
        "Там вообще нет животных, это две змеи",
        "Питон",
        "Удав",
        "Кобра"
    ),
    Question(
        "Сколько времени требуется солнечному свету, чтобы долететь до Земли?",
        "Около 8 минут",
        "Меньше секунды",
        "Примерно 24 часа",
        "Свет долетает мгновенно"
    ),
    Question(
        "Какой металл является единственным, который остается жидким при комнатной температуре?",
        "Ртуть",
        "Галлий",
        "Франций",
        "Цезий"
    ),
    Question(
        "В честь какого персонажа или объекта была названа компания Bluetooth?",
        "Скандинавского короля Харальда Синезубого",
        "Синего кита из древней легенды",
        "Первого черничного пирога",
        "Марки редких синих чернил"
    )
]

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

# Функционал приложения 
def ask(question):
    pass

def show_result():
    pass

def show_question():
    pass

def check_answer():
    pass

def next_question():
    pass

def click_ok():
    pass

ok_button.clicked.connect(click_ok)

# Запуск приложения
window.show()
app.exec()
