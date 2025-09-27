from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

Window.clearcolor = (1,1,1,1)

class StartScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        layout = BoxLayout(orientation='vertical')
        title = Label(text='Тест на слабоумие', font_size='50px', color=(0,0,0,1))
        button = Button(text='Начать', font_size='30px', size_hint=(0.8, 0.4), pos_hint={'center_x': 0.5}, background_color=(0,1,0,1))
        button.on_press = self.start_quiz
        layout.add_widget(title)
        layout.add_widget(button)
        self.add_widget(layout)

    def start_quiz(self):
        self.manager.current = 'question'

class QuestionScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        question = Label(text='Сколько будет 2 + 2', font_size='50px')
        self.add_widget(question)

class ResultScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        result = Label(text='Правильно', font_size='50px')
        self.add_widget(result)

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget( StartScreen(name='start') )
        screen_manager.add_widget( QuestionScreen(name='question') )
        screen_manager.add_widget( ResultScreen(name='result') )
        return screen_manager

app = MyApp()
app.run()
