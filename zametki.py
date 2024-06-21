from PyQt5.QtWidgets import (
    QWidget, QApplication, QTextEdit, QHBoxLayout)

#ИНТЕРФЕЙС ПРИЛОЖЕНИЯ
app = QApplication([]) # создаем приложение
window = QWidget()     # создаем главное окно
window.setWindowTitle('Гениальные заметки') #меняем заголовок окна

text_field = QTextEdit() # поле для ввода текста
#РАЗМЕЩЕНИЕ ИНТЕРФЕЙСА
main_layout = QHBoxLayout() # создаем главную линию
main_layout.addWidget(text_field) # добавляем виджет
#ЗАПУСК ПРИЛОЖЕНИЯ
window.setLayout(main_layout) # установка главной линии
window.show() # отображение окна
app.exec() # не закрывать приложение пока не нажмем на крестик
