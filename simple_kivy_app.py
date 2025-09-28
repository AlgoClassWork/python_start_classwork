from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

Window.clearcolor = (1, 1, 1, 1)
Window.size = (400, 600)

class StartScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        layout = BoxLayout(orientation='vertical', padding=50)
        title = Label(text='Тест на \n слабоумие', color=(0, 0, 0, 1), font_size='50px', halign ='center')
        button = Button(text='Начать', font_size='30px', background_color=(0.5, 1, 0.5, 1), size_hint=(0.75, 0.25), pos_hint={'center_x': 0.5})
        button.on_press = self.start_quiz
        layout.add_widget(title)
        layout.add_widget(button)
        self.add_widget(layout)

    def start_quiz(self):
        self.manager.current = 'question'

class QuestionScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        question = Label(text='Сколько вам лет?', color=(0,0,0,1), font_size='30px')
        button1 = Button(text='500', font_size='20px', background_color=(0.5, 0.5, 1, 1), size_hint=(1, 0.2))
        button2 = Button(text='-1', font_size='20px', background_color=(0.5, 0.5, 1, 1), size_hint=(1, 0.2))
        button3 = Button(text='Низнаю', font_size='20px', background_color=(0.5, 0.5, 1, 1), size_hint=(1, 0.2))
        button4 = Button(text='Другое', font_size='20px', background_color=(0.5, 0.5, 1, 1), size_hint=(1, 0.2))
        button1.on_press = self.show_result
        button2.on_press = self.show_result
        button3.on_press = self.show_result
        button4.on_press = self.show_result
        layout.add_widget(question)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.add_widget(layout)

    def show_result(self):
        self.manager.current = 'result'

class ResultScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(StartScreen(name='start'))
        screen_manager.add_widget(QuestionScreen(name='question'))
        screen_manager.add_widget(ResultScreen(name='result'))
        return screen_manager

app = MyApp()
app.run()
