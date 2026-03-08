import os
import PyQt5
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

# Чтобы работал PyQt5
pyqt_path = os.path.dirname(PyQt5.__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(pyqt_path, "Qt5", "plugins", "platforms")

# Инициализация
app = QApplication([])
window = QWidget()
window.setWindowTitle("Генератор победителей")
window.resize(450, 300) # Задаем приятный начальный размер окна

# Создание виджетов
text = QLabel("Нажмите на кнопку,\nчтобы узнать счастливчика!")
text.setAlignment(Qt.AlignCenter) # Центрируем текст

winner = QLabel("Победитель: ?")
winner.setAlignment(Qt.AlignCenter)

button = QPushButton("Сгенерировать победителя")
button.setCursor(Qt.PointingHandCursor) # Делаем курсор в виде "руки" при наведении

# --- Настройка стилей (QSS) ---

# Общий фон окна
window.setStyleSheet("background-color: #F4F7FC;")

# Стиль верхнего текста
text.setStyleSheet("""
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 24px;
    font-weight: 600;
    color: #334155;
""")

# Стиль текста победителя
winner.setStyleSheet("""
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 42px;
    font-weight: bold;
    color: #10B981; /* Приятный изумрудный цвет */
    margin: 20px 0px;
""")

# Стиль кнопки с состояниями (обычное, наведение, нажатие)
button.setStyleSheet("""
    QPushButton {
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 20px;
        font-weight: bold;
        padding: 15px 30px;
        background-color: #3B82F6;
        color: white;
        border: none;
        border-radius: 12px;
    }
    QPushButton:hover {
        background-color: #2563EB; /* Темнеет при наведении */
    }
    QPushButton:pressed {
        background-color: #1D4ED8; /* Еще темнее при клике */
    }
""")

# --- Размещение (Layout) ---
layout = QVBoxLayout()
layout.addWidget(text)
layout.addWidget(winner)
layout.addWidget(button)

# Настройка отступов внутри окна
layout.setContentsMargins(40, 40, 40, 40)
layout.setSpacing(20) # Расстояние между элементами
window.setLayout(layout)

# Функция генерации победителя
def generate_winner():
    winner_number = random.randint(1, 100)
    winner.setText(f"Победитель: {winner_number}")

button.clicked.connect(generate_winner)

# Запуск
window.show()
app.exec()
