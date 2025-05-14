from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel)

app = QApplication([])

# Применяем стили ко всему приложению
app.setStyleSheet("""
    QWidget {
        font-family: 'Segoe UI', Arial, sans-serif; /* Используем более современный шрифт */
        font-size: 11pt; /* Базовый размер шрифта */
        background-color: #f0f0f0; /* Светлый фон для окна */
    }

    QGroupBox {
        background-color: #ffffff; /* Белый фон для групп */
        border: 1px solid #cccccc;
        border-radius: 8px;
        margin-top: 1ex; /* Отступ сверху для заголовка */
        padding: 15px; /* Внутренние отступы */
    }

    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top center; /* Заголовок по центру */
        padding: 0 10px;
        background-color: #007bff; /* Синий цвет для фона заголовка */
        color: white; /* Белый цвет текста заголовка */
        border-radius: 4px;
        font-weight: bold;
    }

    QLabel#lb_Question { /* Специфичный стиль для метки с вопросом */
        font-size: 16pt;
        font-weight: bold;
        color: #333333;
        padding: 10px;
        qproperty-alignment: 'AlignCenter'; /* Выравнивание текста по центру */
        background-color: transparent; /* Убираем фон по умолчанию от QWidget */
    }

    QLabel {
        color: #444444; /* Темно-серый цвет для обычных меток */
        background-color: transparent; /* Убираем фон по умолчанию от QWidget */
    }

    QPushButton {
        background-color: #007bff; /* Основной синий цвет */
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 12pt;
        border-radius: 5px;
        min-height: 20px; /* Минимальная высота кнопки */
    }

    QPushButton:hover {
        background-color: #0056b3; /* Темнее при наведении */
    }

    QPushButton:pressed {
        background-color: #004085; /* Еще темнее при нажатии */
    }

    QRadioButton {
        spacing: 8px; /* Расстояние между индикатором и текстом */
        color: #333333;
        background-color: transparent; /* Убираем фон по умолчанию от QWidget */
        padding: 2px;
    }

    QRadioButton::indicator {
        width: 18px;  /* Размер индикатора */
        height: 18px;
    }

    QRadioButton::indicator::unchecked {
        border: 2px solid #999999;
        border-radius: 9px;
        background-color: white;
    }

    QRadioButton::indicator::unchecked:hover {
        border: 2px solid #007bff;
    }

    QRadioButton::indicator::checked {
        border: 2px solid #007bff;
        border-radius: 9px;
        background-color: #007bff; /* Синий фон для выбранного */
        /* Можно добавить внутренний кружок для лучшего вида */
        image: none; /* Убираем стандартное изображение, если оно есть */
    }
    
    /* Для отображения "точки" внутри выбранного радио-баттона */
    QRadioButton::indicator::checked::after {
        content: '';
        display: block;
        width: 8px;
        height: 8px;
        margin: 3px; /* (18-2*2-8)/2 = 3 чтобы было по центру, где 2*2 - border width*/
        border-radius: 4px;
        background-color: white;
    }

""")


# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
lb_Question.setObjectName("lb_Question") # Добавляем ID для специфичного стиля

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(15) # Немного увеличим интервалы для нового стиля

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.resize(500, 450) # Сделаем окно немного больше для лучшего отображения стилей
window.show()

app.exec()
