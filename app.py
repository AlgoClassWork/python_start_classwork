from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QVBoxLayout , QRadioButton, QHBoxLayout, QMessageBox
)

#ЭЛЕМЕНТЫ ИНТЕРФЕЙСА
app = QApplication([])
window = QWidget()
window.setWindowTitle('Викторина для особо одаренных')
window.resize(400,200)
window.setStyleSheet('QWidget {background-color: yellow}')
question = QLabel('Кто сигма ???')
question.setStyleSheet('QLabel {font-size:30px}')
rbutton1 = QRadioButton('Адольф')
rbutton1.setStyleSheet('QRadioButton {font-size:20px}')
rbutton2 = QRadioButton('Володя')
rbutton2.setStyleSheet('QRadioButton {font-size:20px}')
rbutton3 = QRadioButton('Джо')
rbutton3.setStyleSheet('QRadioButton {font-size:20px}')
rbutton4 = QRadioButton('Пикачу')
rbutton4.setStyleSheet('QRadioButton {font-size:20px}')
#РАЗМЕЩЕНИЕ ИНТЕРФЕЙСА
main_layout = QVBoxLayout()
main_layout.addWidget(question,alignment=Qt.AlignCenter)
h1 = QHBoxLayout()
h1.addWidget(rbutton1,alignment=Qt.AlignCenter)
h1.addWidget(rbutton2,alignment=Qt.AlignCenter)
main_layout.addLayout(h1)
h2 = QHBoxLayout()
h2.addWidget(rbutton3,alignment=Qt.AlignCenter)
h2.addWidget(rbutton4,alignment=Qt.AlignCenter)
main_layout.addLayout(h2)
#ФУНКЦИОНАЛ
def show_win():
    win = QMessageBox()
    win.setText('Вы выиграли раба')
    win.exec()
def show_lose():
    lose = QMessageBox()
    lose.setText('Вы выиграли пачку сухариков')
    lose.exec()
#ПОДПИСКИ НА СОБЫТИЯ
rbutton1.clicked.connect(show_lose)
rbutton2.clicked.connect(show_lose)
rbutton3.clicked.connect(show_lose)
rbutton4.clicked.connect(show_win)
#ЗАПУСК ПРИЛОЖЕНИЯ
window.setLayout(main_layout)
window.show()
app.exec()
