from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        test_name = Label(text="ТЕСТ НА СЛАБОУМИЕ")
        test_info = Label(text="Это шуточный тест. Он не претендует на медецинскую точность\n"
                          "Пройдите тест, чтобы узнать свой результат")
        start_button = Button(text="Начать тест")
        layout.add_widget(test_name)
        layout.add_widget(test_info)
        layout.add_widget(start_button)
        return layout

app = TestApp()
app.run()
