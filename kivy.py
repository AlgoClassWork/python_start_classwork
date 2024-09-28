from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        box = BoxLayout()
        btn = Button(text="Переключиться на другой экран")
        btn.on_press = self.next
        txt = Label(text="Первый экран")
        box.add_widget(txt)
        box.add_widget(btn)
        self.add_widget(box)

    def next(self):
        self.manager.transition.direction = 'left' 
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        box = BoxLayout()
        btn = Button(text="Переключиться на другой экран")
        btn.on_press = self.next
        txt = Label(text="Второй экран")
        box.add_widget(btn)
        box.add_widget(txt)
        self.add_widget(box)

    def next(self):
        self.manager.transition.direction = 'right' 
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        screens = ScreenManager()
        screens.add_widget(FirstScr())
        screens.add_widget(SecondScr())
        return screens

app = MyApp()
app.run()
