from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.9,0.9,1,1)

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        test_name = Label(text="ТЕСТ НА СЛАБОУМИЕ", font_size="80px", color=(0.9,0,0,1))
        test_info = Label(text="Это шуточный тест. Он не претендует на медецинскую точность\n"
                          "Пройдите тест, чтобы узнать свой результат",
                          font_size="30px",
                          color=(0,0,0,1),
                          halign="center")
        start_button = Button(text="Начать тест",
                              background_color=(0.5,1,0.5,1),
                              size_hint=(0.5,0.2),
                              pos_hint={'center_x': 0.5})
        layout.add_widget(test_name)
        layout.add_widget(test_info)
        layout.add_widget(start_button)
        return layout

app = TestApp()
app.run()
