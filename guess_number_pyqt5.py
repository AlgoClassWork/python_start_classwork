import os
from random import randint
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

# Твой фикс для платформы
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Угадай число")
window.setMinimumSize(350, 250)  # Задаем комфортный начальный размер

# --- СТИЛИЗАЦИЯ (QSS) ---
ModernStyle = """
    QWidget {
        background-color: #1e1e2e;  /* Глубокий тёмный фон */
        font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    }
    
    QLabel {
        color: #cdd6f4;             /* Светлый приятный текст */
        font-size: 18px;
        font-weight: bold;
        qproperty-alignment: AlignCenter; /* Центровка текста */
        margin-bottom: 10px;
    }
    
    QLineEdit {
        background-color: #313244;  /* Чуть светлее фона для контраста */
        color: #a6e3a1;             /* Зеленоватый текст для вводимых цифр */
        font-size: 20px;
        border: 2px solid #45475a;
        border-radius: 10px;        /* Скругление углов */
        padding: 8px;
        font-weight: bold;
        qproperty-alignment: AlignCenter;
    }
    
    QLineEdit:focus {
        border: 2px solid #cba6f7;  /* Подсветка поля при клике (фиолетовая) */
    }
    
    QPushButton {
        background-color: #89b4fa;  /* Приятный синий цвет */
        color: #11111b;             /* Тёмный текст на кнопке */
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 12px;
        margin-top: 10px;
    }
    
    QPushButton:hover {
        background-color: #b4befe;  /* Эффект при наведении мышкой */
    }
    
    QPushButton:pressed {
        background-color: #74c7ec;  /* Эффект при клике */
    }
"""
app.setStyleSheet(ModernStyle)
# ------------------------

label = QLabel("Угадай число\nот 1 до 100")
input_field = QLineEdit()
input_field.setPlaceholderText("?") # Подсказка внутри пустого поля

button = QPushButton("Проверить")

# Настраиваем отступы в лейауте, чтобы элементам не было тесно
layout = QVBoxLayout()
layout.setContentsMargins(30, 30, 30, 30) 
layout.setSpacing(15)

window.setLayout(layout)
layout.addWidget(label)
layout.addWidget(input_field)
layout.addWidget(button)


# Подписка на событие нажатия кнопки
secret_number = randint(1, 100)  # Случайное число от 1 до 100

def check_number():
    number = input_field.text()
    if not number.isdigit():
        label.setText("Пожалуйста, введите число!")
        return
    number = int(number)
    if number < secret_number:
        label.setText("Слишком мало! Попробуй ещё.")
    elif number > secret_number:
        label.setText("Слишком много! Попробуй ещё.")
    else:
        label.setText("Поздравляю! Ты угадал число!")
    

button.clicked.connect(check_number)

window.show()
app.exec()
