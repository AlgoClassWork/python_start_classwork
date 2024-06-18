from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QRadioButton,
    QGroupBox, QButtonGroup)


class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meme Card')
        self.init_ui()
        self.resize(400,300)
        self.show()

    def init_ui(self):
        self.setStyleSheet("""QWidget {
                            font-size: 20px;}
                            QPushButton {
                            font-size: 20px;
                            background-color: green;
                            color: white;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            margin: 4px 2px;
                            cursor: pointer;
                            border-radius: 12px;
                            }
                            QLabel {
                                font-size:25px;
                            }
                           QGroupBox {
                           font-size: 18px;
                           font-weight: bold;
                           }""")
        self.btn_OK = QPushButton('Ответить')
        self.question = QLabel('Самый сложный вопрос в мире!')

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

        self.layout_ans1 = QHBoxLayout()
        self.layout_ans2 = QVBoxLayout()
        self.layout_ans3 = QVBoxLayout()
        self.layout_ans2.addWidget(self.rbtn_1)
        self.layout_ans2.addWidget(self.rbtn_2)
        self.layout_ans3.addWidget(self.rbtn_3)
        self.layout_ans3.addWidget(self.rbtn_4)

        self.layout_ans1.addLayout(self.layout_ans2)
        self.layout_ans1.addLayout(self.layout_ans3)
        self.RadioGroupBox.setLayout(self.layout_ans1)

        layout_line1 = QHBoxLayout()
        layout_line2 = QHBoxLayout()
        layout_line3 = QHBoxLayout()

        layout_line1.addWidget(self.question)
        layout_line2.addWidget(self.RadioGroupBox)

        layout_line3.addWidget(self.btn_OK, stretch=2)

        layout_card = QVBoxLayout()
        layout_card.addLayout(layout_line1,stretch=2)
        layout_card.addLayout(layout_line2,stretch=6)
        layout_card.addLayout(layout_line3,stretch=1)
        layout_card.setSpacing(5)

        self.setLayout(layout_card)


app = QApplication([])
window = QuizApp()
app.exec()
