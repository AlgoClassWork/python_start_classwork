from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QRadioButton, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt

# Создание приложения
app = QApplication([])

# Создание главного окна
window = QWidget()
window2 = QWidget()
window.setWindowTitle('Тест на ICQ')
window.setStyleSheet('background-color: #f0f8ff;') 

# СОЗДАНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА
question_label = QLabel('Какого цвета чернокожие?')
question_label.setStyleSheet('font-size: 28px; font-weight: bold; color: #333; margin-bottom: 30px; text-align: center;')

rbtn1 = QRadioButton('Белые')
rbtn1.setStyleSheet('font-size: 18px; color: #555; margin-right: 50px; margin-bottom: 15px;')

rbtn2 = QRadioButton('Зеленые')
rbtn2.setStyleSheet('font-size: 18px; color: #555; margin-bottom: 15px;')

rbtn3 = QRadioButton('Голубые')
rbtn3.setStyleSheet('font-size: 18px; color: #555; margin-right: 50px; margin-bottom: 15px;')

rbtn4 = QRadioButton('Черные')
rbtn4.setStyleSheet('font-size: 18px; color: #555; margin-bottom: 15px;')

button = QPushButton('Ответить')
button.setStyleSheet(
    'background-color: #5cb85c; color: white; padding: 12px 25px; '
    'font-size: 20px; border: none; border-radius: 7px; font-weight: bold;'
)
button.setCursor(Qt.PointingHandCursor)

question_label2 = QLabel('Какого цвета чернокожие?')
result_label = QLabel('Правильно')
button2 = QPushButton('Следующий вопрос')

# РАЗМЕЩЕНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА
main_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()

main_line.addWidget(question_label)

main_line.addLayout(h1_line)
main_line.addLayout(h2_line)

main_line.addWidget(button)
main_line.setAlignment(Qt.AlignCenter) # Выравнивание по центру

h1_line.addWidget(rbtn1)
h1_line.addWidget(rbtn2)
h1_line.setAlignment(Qt.AlignCenter) # Выравнивание по центру

h2_line.addWidget(rbtn3)
h2_line.addWidget(rbtn4)
h2_line.setAlignment(Qt.AlignCenter) # Выравнивание по центру

window.setLayout(main_line)

main_line2 = QVBoxLayout()
main_line2.addWidget(question_label2)
main_line2.addWidget(result_label)
main_line2.addWidget(button2)
window2.setLayout(main_line2)
# ЗАПУСК ПРИЛОЖЕНИЯ
window.show()
window2.show()
app.exec()
