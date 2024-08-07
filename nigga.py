from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout)
from random import choice


names = [
    "Белекова Элина",
    "Исакова Айбийке",
    "Качкынов эмир",
    "Кожомбердиев Эльхан",
    "Лебедев Василий",
    "Мешанло Эмир",
    "Самудинова Акылай",
    "Суюнбаев Эльхан",
    "Токталыев Руслан",
    "Токтосунов Нурлан",
    "Хидернабиев Махьди",
    "Шарипова Адина",
    "Кухестани Артем"
]

#создание виджетов
app = QApplication([])
window = QWidget()

text = QLabel('Узнай кто нигга!')
button = QPushButton('Нажми на меня')
#стилизация
window.setStyleSheet('''
QLabel {font-size:40px;padding:10px}
QPushButton {background-color:black;color:white;font-size:30px;padding:10px}
''')

#размещение
line = QVBoxLayout()
line.addWidget(text)
line.addWidget(button)

window.setLayout(line)
#функционал
def show_nigga():
    text.setText('Нигга по имени: '+ choice(names))
#подписка на события
button.clicked.connect(show_nigga)

#запуск приложения
window.show()
app.exec()
