from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class MyButton(Button):
    def __init__(self, screen, goal, **data):
        super().__init__(**data)
        self.screen = screen
        self.goal = goal
    
    def on_press(self):
        self.screen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        label = Label(text='Выбери экран')
        layout = BoxLayout()
        button_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        button_layout.add_widget( MyButton(self, goal='first', text='1') )
        button_layout.add_widget( MyButton(self, goal='second', text='2') )
        button_layout.add_widget( MyButton(self, goal='third', text='3') )
        button_layout.add_widget( MyButton(self, goal='fourth', text='4') )

        layout.add_widget(label)
        layout.add_widget(button_layout)

        self.add_widget(layout)

class FirstScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        button = Button(text='Выбор', size_hint=(1, 0.5),)
        back_button = MyButton(self, goal='main', text='Назад',
                        size_hint=(1, 0.5),pos_hint={'center_y':0.75}) 
        layout = BoxLayout(size_hint=(0.5, 0.5),
                           pos_hint={'center_x':0.5,'center_y':0.5})
        layout.add_widget(button)
        layout.add_widget(back_button)
        self.add_widget(layout)

class ThirdScreen(Screen):
    def __init__(self, **data):
        super().__init__(**data)
        label = Label(text='Твой экран')
        back_button = MyButton(self, goal='main', text='Назад', size_hint=(1, 0.1)) 
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget( MainScreen(name='main') )
        screen_manager.add_widget( FirstScreen(name='first') )
        screen_manager.add_widget( ThirdScreen(name='third') )
        return screen_manager
    
app = MyApp()
app.run()
