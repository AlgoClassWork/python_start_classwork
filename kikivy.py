from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

class MyButton(Button):
    def __init__(self, screen, direction, goal, **data):
        super().__init__(**data)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        main_layout = BoxLayout()
        button_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        text = Label(text='Выбери экран')
        button_layout.add_widget( MyButton(self, direction='down', goal='first', text='1') )
        button_layout.add_widget( MyButton(self, direction='left', goal='second', text='2') )
        button_layout.add_widget( MyButton(self, direction='up', goal='third', text='3') )
        button_layout.add_widget( MyButton(self, direction='right', goal='fourth', text='4') )
        main_layout.add_widget(text)
        main_layout.add_widget(button_layout)
        self.add_widget(main_layout)

class FirstScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        main_layout = BoxLayout(orientation='vertical', size_hint=(0.5, 0.5), pos_hint={'center_x':0.5, 'center_y':0.5})
        button = Button(text='Выбор', size_hint=(0.5, 1), pos_hint={'left': 0} )
        button_back = MyButton(self, direction='up', goal='main', text='назад', size_hint=(0.5, 1), pos_hint={'right': 1})
        main_layout.add_widget(button)
        main_layout.add_widget(button_back)
        self.add_widget(main_layout)

class SecondScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        main_layout = BoxLayout(orientation='vertical')
        h1 = BoxLayout(size_hint=(0.7, None), height='50px', pos_hint={'center_x':0.5})
        h2 = BoxLayout(size_hint=(0.7, None), height='100px', pos_hint={'center_x':0.5})
        self.label = Label(text='Выбор')
        text_input = Label(text='Введите пароль')
        self.password_input = TextInput()
        button = Button(text='OK')
        button_back = MyButton(self, direction='right', goal='main', text='назад')
        h1.add_widget(text_input)
        h1.add_widget(self.password_input)
        h2.add_widget(button)
        h2.add_widget(button_back)
        main_layout.add_widget(self.label)
        main_layout.add_widget(h1)
        main_layout.add_widget(h2)
        self.add_widget(main_layout)

        button.on_press = self.change_text

    def change_text(self):
        self.label.text = self.password_input.text + ' Не сработал'

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget( MainScreen(name='main') )
        screen_manager.add_widget( FirstScreen(name='first') )
        screen_manager.add_widget( SecondScreen(name='second') )
        return screen_manager

app = MyApp()
app.run()
