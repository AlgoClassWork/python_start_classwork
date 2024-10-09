import json
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
        start_button.bind(on_press=self.change_screen)
        layout.add_widget(test_name)
        layout.add_widget(test_info)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def change_screen(self, instanse):
        app = App.get_running_app()
        app.screen_manager.current = 'question_0'

class QuestionScreen(Screen):
    def __init__(self,data,index,**kwargs):
        super().__init__(**kwargs)
        self.name = f'question_{index}'
        self.data = data
        self.index = index
        question_label = Label(text=data['question'])
        line = BoxLayout(orientation='vertical')
        line.add_widget(question_label)
        for option in data['options']:
            button = Button(text=option['text'])
            line.add_widget(button)
        self.add_widget(line)


class TestApp(App):
    def build(self):
        with open('questions.json','r',encoding='utf-8') as file:
            self.questions = json.load(file)

        self.screen_manager = ScreenManager()

        self.screen_manager.add_widget(StartScreen(name="start"))
        for index, data in enumerate(self.questions):
            screen = QuestionScreen(data=data,index=index)
            self.screen_manager.add_widget(screen)
        
        self.screen_manager.current = "start"
        return self.screen_manager
    
app = TestApp()
app.run()
