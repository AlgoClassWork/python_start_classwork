import json
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


# Задаем главный цвет нашего приложения
Window.clearcolor = (0.95,0.95,1,1)


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical',padding=20, spacing=20)
        title_label = Label(text='Тест на слабоумие',font_size='60px', color=(0,0,0,1))
        description_label = Label(text= 'Это шуточный тест.\n'
                                        'Он не претендует на медецинскую точность\n'
                                        'Пройдите его, чтобы узнать свой результат!',
        font_size='40px', color=(0,0,0,1), halign = 'center')
        start_button = Button(text='Начать тест',
                              size_hint=(0.5,0.2),
                              pos_hint={'center_x': 0.5},
                              background_color = (0,0,0,1))
        start_button.bind(on_press = self.start_test) 
        layout.add_widget(title_label)
        layout.add_widget(description_label)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def start_test(self, instanse):
        app = App.get_running_app()
        app.screen_manager.current = 'question_0'

class QuestionScreen(Screen):
    def __init__(self, data, index, **kwargs):
        super().__init__(**kwargs)
        self.name = f'question_{index}'
        self.data = data
        self.index = index
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        question = Label(text = data['question'], font_size='40px', color=(0,0,0,1))
        layout.add_widget(question)
        for option in data['options']:
            answer = Button(text = option['text'],
                            font_size='30px',
                            size_hint=(0.8,0.2),
                            pos_hint={'center_x': 0.5},
                            background_color = (0,0,0,1))
            layout.add_widget(answer)
        self.add_widget(layout)

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'result_screen'
        layout = BoxLayout(orientation='vertical',padding = 20, spacing=20)
        result_text = Label(text="Здесь будет результат вашего тестирования",
                       font_size='40px', color=(0,0,0,1))
        layout.add_widget(result_text)
        retry_button = Button(text='Попробовать снова',
                        font_size='30px',
                        size_hint=(0.8,0.2),
                        pos_hint={'center_x': 0.5},
                        background_color = (0,0,0,1))
        layout.add_widget(retry_button)
        retry_button.bind(on_press= self.retry_test)
        self.add_widget(layout)

    def retry_test(self, instanse):
        app = App.get_running_app()
        app.answers = []
        app.screen_manager.current = 'start_screen'


class TestApp(App):
    def build(self):
        with open('questions.json','r', encoding='utf-8') as file:
            self.questions = json.load(file)

        self.answers = []

        self.screen_manager = ScreenManager()

        self.screen_manager.add_widget(StartScreen(name='start_screen'))

        for index, data in enumerate(self.questions):
            screen = QuestionScreen(data=data,index = index)
            self.screen_manager.add_widget(screen)

        self.screen_manager.add_widget(ResultScreen())

        self.screen_manager.current = 'result_screen'
        return self.screen_manager

app = TestApp()
app.run()


