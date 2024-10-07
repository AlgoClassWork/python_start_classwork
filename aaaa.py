from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.clearcolor = (0.9,0.9,1,1)

class StartScreen(Screen):
    def __init__(self,**data):
        super().__init__(**data)
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
        self.add_widget(layout)

class SecondScreen(Screen):
    def __init__(self,**data):
        super().__init__(**data)
        layout = BoxLayout(orientation="vertical")
        test_name = Label(text="ЭКРАН НОМЕР 2", font_size="80px", color=(0.9,0,0,1))
        layout.add_widget(test_name)
        self.add_widget(layout)

class TestApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(StartScreen(name="start"))
        screen_manager.add_widget(SecondScreen(name="test"))
        screen_manager.current = "start"
        return screen_manager

app = TestApp()
app.run()
