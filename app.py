from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QRadioButton,
    QGroupBox, QButtonGroup
)

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meme Card')

    def init_ui(self):
        self.btn_OK = QPushButton('Ответить')
        self.question = QLabel('Самый сложный вопрос в мире!')
        self.question.setAlignment(Qt.AligmentHCenter | Qt.AlignmentVCenter)

        self.RadioGroupBox = QGroupBox('Варианты ответов')
        self.rbtn_1 = QRadioButton('вариант 1')
        self.rbtn_2 = QRadioButton('вариант 2')
        self.rbtn_3 = QRadioButton('вариант 3')
        self.rbtn_4 = QRadioButton('вариант 4')

        self.RadioGroup = QButtonGroup()
        self.RadioGroup.addButton(self.rbtn_1)
        self.RadioGroup.addButton(self.rbtn_2)
        self.RadioGroup.addButton(self.rbtn_3)
        self.RadioGroup.addButton(self.rbtn_4)


