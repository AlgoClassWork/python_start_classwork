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

        button.bind(on_press=self.start_test)

        self.add_widget(layout)

    def start_test(self, instance):
        app = App.get_running_app()
        app.sm.current = 'question'

class QuestionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        question = Label(text='Какого цвета негр?', font_size='60px')
        answer1 = Button(text='белый')
        answer2 = Button(text='черный')
        button_layout = BoxLayout()
        button_layout.add_widget(answer1)
        button_layout.add_widget(answer2)
        layout.add_widget(question)
        layout.add_widget(button_layout)

        answer1.bind(on_press=self.lose)
        answer2.bind(on_press=self.win)

        self.add_widget(layout)

    def lose(self, instance):
        app = App.get_running_app()
        app.sm.current = 'wrong'

    def win(self, instance):
        app = App.get_running_app()
        app.sm.current = 'right'

class RightScreen(Screen):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        right = Label(text='Поздравляем теперь вы черный', font_size='40px')
        layout.add_widget(right)
        self.add_widget(layout)

class WrongScreen(Screen):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        wrong = Label(text='Сам ты белый!', font_size='80px')
        layout.add_widget(wrong)
        self.add_widget(layout)


class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(FirstScreen(name='first'))
        self.sm.add_widget(QuestionScreen(name='question'))
        self.sm.add_widget(RightScreen(name='right'))
        self.sm.add_widget(WrongScreen(name='wrong'))
        self.sm.current = 'first'
        return self.sm
    
app = MyApp()
app.run()
