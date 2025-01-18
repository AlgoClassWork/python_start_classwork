from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
#pip install kivy

#Window.clearcolor = (0.95, 0.95, 1, 1)
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        title = Label(text='Тест', font_size='60px')
        button = Button(text='Нажми', size_hint=(0.5, 0.2),
                                      pos_hint={'center_x':0.5},
                                      background_color=(0,1,0,1))
        layout.add_widget(title)
        layout.add_widget(button)
        self.add_widget(layout)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen())
        return sm
    
app = MyApp()
app.run()
