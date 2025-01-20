from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class QuestionScreen(Screen):
    def __init__(self, name='question'):
        super().__init__(name=name)
        label = Label(text='Какого цвета чернокожие?', font_size='50px')
        button = Button(text='Белый', size_hint=(1,0.5))
        button2 = Button(text='Черный', size_hint=(1,0.5))
        layout = BoxLayout(orientation='vertical')
        layout_button = BoxLayout()
        layout_button.add_widget(button)
        layout_button.add_widget(button2)
        layout.add_widget(label)
        layout.add_widget(layout_button)
        self.add_widget(layout)

class WrongScreen(Screen):
    def __init__(self, name='wrong'):
        super().__init__(name=name)
        label = Label(text='Сам ты белый', font_size='50px')
        self.add_widget(label)

class CorrectScreen(Screen):
    def __init__(self, name='correct'):
        super().__init__(name=name)
        label = Label(text='Поздравляем теперь ты черный', font_size='50px')
        self.add_widget(label)

class TestApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(QuestionScreen())
        screen_manager.add_widget(WrongScreen())
        screen_manager.add_widget(CorrectScreen())
        return screen_manager

app = TestApp()
app.run()
