from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class MyButton(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout()
        button_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        text = Label(text='Выбери экран')

        button_layout.add_widget( MyButton(self, 'down', 'first', text='1') )
        button_layout.add_widget( MyButton(self, 'left', 'second', text='2') )
        button_layout.add_widget( MyButton(self, 'up', 'third', text='3') )
        button_layout.add_widget( MyButton(self, 'right', 'fourth', text='4') )

        main_layout.add_widget(text)
        main_layout.add_widget(button_layout)

        self.add_widget(main_layout)


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical',
        size_hint=(0.5, 0.5), pos_hint={'center_x':0.5, 'center_y':0.5})

        button = Button(text='Выбор', size_hint=(0.5, 1), pos_hint={'left' : 0,})
        back_button = MyButton(self, 'up', 'main', text='Назад',
        size_hint=(0.5, 1), pos_hint={'right' : 1,})
        
        main_layout.add_widget(button)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical')

        text = Label(text='Твой экран')
        back_button = MyButton(self, 'down', 'main', text='Назад', size_hint=(1, 0.1))
        
        main_layout.add_widget(text)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget( MainScreen(name='main') )
        screen_manager.add_widget( FirstScreen(name='first') )
        screen_manager.add_widget( ThirdScreen(name='third') )
        return screen_manager

app = MyApp()
app.run()
