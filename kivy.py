#pip install kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class FirstScreen(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        label = Label(text='Какого цвета чернокожий?', font_size='60px')
        button = Button(text='Белый', size_hint=(0.8, 0.4), color=(1,1,1,1))
        button2 = Button(text='Черный', size_hint=(0.8, 0.4), color=(0,0,0,1))

        layout = BoxLayout(orientation='vertical')
        button_layout = BoxLayout()

        layout.add_widget(label)
        button_layout.add_widget(button)
        button_layout.add_widget(button2)
        layout.add_widget(button_layout)

        self.add_widget(layout)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(FirstScreen())
        return screen_manager

app = MyApp()
app.run()
