from random import randint
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel, QGroupBox,
    QRadioButton, QPushButton,
)
from PyQt5.QtCore import Qt

# Хранение данных
class Question():
    def __init__(self, question, correct, wrong1, wrong2, wrong3):
        self.question = question
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = [
    Question('Сколько уток нужно, чтобы починить трактор?', 'Ни одной, у них лапки', 'Пять', 'Семнадцать', 'Три с половиной'),
    Question('Почему коты не летают?', 'У них нет крыльев', 'Они ленивые', 'Боятся высоты', 'Потому что вчера был понедельник'),
    Question('Что будет, если нажать на кнопку "ничего"?', 'Ничего', 'Взрыв', 'Запуск Windows 95', 'Открытие портала в тапки'),
    Question('Сколько понедельников в одном мармеладе?', 'Ни одного', 'Семь', 'Три штуки', 'Вкус клубники'),
    Question('Почему холодильник не разговаривает?', 'Он застенчивый', 'Не знает язык', 'Боится микроволновки', 'Он просто устал'),
    Question('Какой звук издаёт квадратный арбуз?', 'Тупой "бум"', 'Мяу', 'Пиксельный хруст', 'Он молчит, он в шоке'),
    Question('Что произойдёт, если кормить принтер морковкой?', 'Он начнёт печатать салаты', 'Сломается', 'Станет сканером', 'Выдаст чек на урожай'),
    Question('Почему лампочка светится?', 'Потому что хочет внимания', 'У неё свидание', 'Скучно в темноте', 'Это магия электричества'),
    Question('Зачем компьютеру тапочки?', 'Чтобы не мёрзли USB-порты', 'Для комфорта', 'Он идёт гулять', 'Чтобы не скользил по столу'),
    Question('Можно ли сварить чай в Wi-Fi?', 'Нет, но можно попробовать', 'Да, если сильно верить', 'Только в микроволновом облаке', 'Wi-Fi не кипит, он парит'),
]

# Создание обьектов интерфейса
app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест на логику 🧠')
window.setMinimumSize(480, 420)

# Присвоим ID для стилизации
label_question = QLabel('❓ Как тебя зовут?')
label_question.setObjectName("QuestionLabel")
label_question.setAlignment(Qt.AlignCenter)

button_ok = QPushButton('ОТВЕТИТЬ')
button_ok.setObjectName("ActionButton")
button_ok.setFixedHeight(50)

# Форма с вариантами ответов
group_answer = QGroupBox('📝 Варианты ответов') # Добавим иконку
group_answer.setObjectName("GroupBoxAnswer")
rbutton1 = QRadioButton('Забыл')
rbutton2 = QRadioButton('Зеленый')
rbutton3 = QRadioButton('Сорок семь')
rbutton4 = QRadioButton('Тут нет моего имени')

# Форма с результатами
group_result = QGroupBox('✅ Результаты') # Добавим иконку
group_result.setObjectName("GroupBoxResult")
label_result = QLabel('⏳ Ожидание...')
label_result.setAlignment(Qt.AlignCenter)
label_result.setObjectName("ResultMainLabel")

label_correct = QLabel('Ответ: (появится здесь)')
label_correct.setAlignment(Qt.AlignCenter)
label_correct.setObjectName("ResultDetailLabel")

# Размещение обьектов интерфейса
line_main = QVBoxLayout()
line_main.setContentsMargins(30, 30, 30, 30)
line_main.setSpacing(20)

# Размещение для формы с вариантами ответов
line_answer_main = QVBoxLayout()
line_answer_h1 = QHBoxLayout()
line_answer_h2 = QHBoxLayout()
line_answer_h1.setSpacing(25)
line_answer_h2.setSpacing(25)

line_answer_main.addLayout(line_answer_h1)
line_answer_main.addLayout(line_answer_h2)

line_answer_h1.addWidget(rbutton1)
line_answer_h1.addWidget(rbutton2)
line_answer_h2.addWidget(rbutton3)
line_answer_h2.addWidget(rbutton4)
group_answer.setLayout(line_answer_main)

# Размещение для формы с результатами
line_result_main = QVBoxLayout()
line_result_main.setSpacing(10)
line_result_main.addWidget(label_result)
line_result_main.addWidget(label_correct)
group_result.setLayout(line_result_main)
group_result.setMinimumHeight(120)

# Размещение всех виджетов
line_main.addWidget(label_question)
line_main.addSpacing(15)
line_main.addWidget(group_answer)
line_main.addWidget(group_result)
line_main.addSpacing(10)
line_main.addWidget(button_ok)

window.setLayout(line_main)

# ✅ Улучшенная Стилизация с акцентом на QGroupBox::title ✅
app.setStyleSheet("""
    /* ------------------- Общий Фон ------------------- */
    QWidget {
        background-color: #f0f4f8; /* Очень светлый, чистый фон */
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 16px;
        color: #334e68; /* Мягкий, но читаемый сине-серый текст */
    }

    /* ------------------- Заголовок Вопроса ------------------- */
    QLabel#QuestionLabel {
        font-size: 24px;
        font-weight: 700;
        color: #007bff; /* Яркий, чистый синий */
        padding: 15px 0;
        margin-bottom: 10px;
    }

    /* ------------------- Блоки Групп (Контейнеры - "Карточки") ------------------- */
    QGroupBox {
        border: 1px solid #c8d1da; /* Тонкая, светлая рамка */
        border-radius: 12px; /* Умеренное скругление */
        padding: 20px;
        /* Важно: Увеличиваем margin-top, чтобы заголовок мог разместиться над рамкой */
        margin-top: 25px; 
        font-weight: 600;
        color: #334e68;
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #ffffff, stop:1 #f8f9fa);
    }

    /* 👑 УЛУЧШЕНИЕ ЗАГОЛОВКА ГРУППЫ (QGroupBox::title) 👑 */
    QGroupBox::title {
        subcontrol-origin: margin;
        top: 10px; 
        /* Стиль плашки/ярлыка */
        padding: 4px 12px;
        border-radius: 8px; /* Скругленные углы плашки */
        font-size: 15px;
        font-weight: bold;
        color: #ffffff; /* Белый текст */
        /* Используем яркий градиент для выделения */
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                    stop:0 #007bff, stop:1 #0056b3); 
    }

    /* ------------------- Радиокнопки ------------------- */
    QRadioButton {
        spacing: 15px;
        padding: 10px;
        border-radius: 8px;
        color: #334e68;
    }

    QRadioButton:hover {
        background-color: #e3f2fd;
    }

    QRadioButton::indicator {
        width: 16px;
        height: 16px;
    }

    QRadioButton::indicator:unchecked {
        border-radius: 8px;
        background-color: #ffffff;
        border: 2px solid #007bff;
    }

    QRadioButton::indicator:checked {
        border-radius: 8px;
        background-color: #007bff;
        border: 2px solid #007bff;
    }

    /* ------------------- Метки Результатов ------------------- */
    QLabel#ResultMainLabel {
        font-size: 20px;
        font-weight: 700;
        color: #28a745;
        padding: 10px 0;
    }

    QLabel#ResultDetailLabel {
        font-size: 16px;
        color: #6c757d;
    }

    /* ------------------- Кнопка ------------------- */
    QPushButton#ActionButton {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #007bff, stop:1 #0056b3);
        color: white;
        padding: 15px 25px;
        border: none;
        border-radius: 25px;
        font-size: 18px;
        font-weight: bold;
    }

    QPushButton#ActionButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #0056b3, stop:1 #004494);
    }

    QPushButton#ActionButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #004494, stop:1 #0056b3);
    }
""")

# Функционал
def show_question():
    group_answer.show()
    group_result.hide()
    button_ok.setText('ОТВЕТИТЬ')

    # Показ нового вопроса
    question = questions[ randint(0, len(questions) - 1) ]
    label_question.setText( question.question )
    rbutton1.setText( question.correct )
    rbutton2.setText( question.wrong1 )
    rbutton3.setText( question.wrong2 )
    rbutton4.setText( question.wrong3 )

def show_result():
    group_answer.hide()
    group_result.show()
    button_ok.setText('Следующий вопрос')
    check_answer()

def check_answer():
    if rbutton4.isChecked():
        label_result.setText('Правильно')
    else:
        label_result.setText('Не правильно')

    label_correct.setText('Тут нет моего имени')

def change_screen():
    if button_ok.text() == 'ОТВЕТИТЬ':
        show_result()
    elif button_ok.text() == 'Следующий вопрос':
        show_question()

button_ok.clicked.connect(change_screen)
# Запуск приложения
group_result.hide()
window.show()
app.exec()
