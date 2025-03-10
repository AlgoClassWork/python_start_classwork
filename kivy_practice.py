from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Button(text='Перейти на второй экран', font_size=50)
        button.on_press = self.next_screen
        self.add_widget(button)

    def next_screen(self):
        self.manager.current = 'second'

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button2 = Button(text='Перейти на первый экран', font_size=50)
        button2.on_press = self.next_screen
        self.add_widget(button2)

    def next_screen(self):
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget( FirstScreen(name='first') )
        screen_manager.add_widget( SecondScreen(name='second') )
        return screen_manager
    
app = MyApp()
app.run()
