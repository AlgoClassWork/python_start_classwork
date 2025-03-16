from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

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

class MyApp(App):
    def build(self):
        return MainScreen()
    
app = MyApp()
app.run()
